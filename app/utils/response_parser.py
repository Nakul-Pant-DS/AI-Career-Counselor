import json
import re

from app.core.logging import logger


class ResponseParser:
    """
    Cleans and validates LLM responses before
    converting them into application objects.
    """

    @staticmethod
    def parse(response: str) -> str:

        logger.info("Parsing LLM response.")

        # Remove markdown code fences
        response = response.replace("```json", "")
        response = response.replace("```", "")

        response = response.strip()

        # Extract JSON object if extra text exists
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if not match:
            logger.error("No JSON object found in LLM response.")
            from app.exceptions.llm_exceptions import InvalidLLMResponseException
            raise InvalidLLMResponseException("No valid JSON found in LLM response.")

        json_string = match.group()

        # Validate JSON
        json.loads(json_string)

        logger.info("Valid JSON extracted successfully.")

        return json_string
