import json

from pydantic import ValidationError
from app.utils.response_parser import ResponseParser

from app.schemas.resume_data import ResumeData
from app.prompts.resume_prompt import build_resume_prompt
from app.services.llm_service import LLMService
from app.core.logging import logger
from app.utils.retry import retry

from app.utils.ai_metrics import AIMetrics
from app.core.config import settings


class ResumeExtractor:

    def __init__(self):

        self.llm = LLMService()

    @retry(max_attempts=3, delay=1)
    def extract(self, resume_text: str) -> ResumeData:

        logger.info("Building extraction prompt.")

        prompt = build_resume_prompt(resume_text)

        logger.info("Calling LLM.")

        start = AIMetrics.start()

        response = self.llm.ask(prompt)

        latency = AIMetrics.stop(start)

        logger.info("LLM response received.")

        try:

            clean_json = ResponseParser.parse(response)

            resume = ResumeData.model_validate_json(response)

            logger.info("Resume successfully validated.")

            AIMetrics.log_metrics(
                model=settings.GROQ_MODEL,
                prompt=prompt,
                response=response,
                latency=latency,
                retries=0,
                validation_success=True
            )

            return resume

        except ValidationError as e:

            logger.error("Resume validation failed.")

            from app.exceptions.llm_exceptions import (LLMValidationException,)

        except json.JSONDecodeError as e:

            logger.error("Invalid JSON returned by LLM.")

            AIMetrics.log_metrics(
                model=settings.GROQ_MODEL,
                prompt=prompt,
                response=response,
                latency=latency,
                retries=0,
                validation_success=False
            )

            raise e
