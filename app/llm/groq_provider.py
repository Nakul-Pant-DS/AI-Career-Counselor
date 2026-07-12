from groq import Groq

from app.core.config import settings
from app.llm.base_provider import BaseLLMProvider
from app.core.logging import logger


class GroqProvider(BaseLLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate(self, prompt: str) -> str:

        logger.info("Sending prompt to Groq.")

        response = self.client.chat.completions.create(

            model=settings.GROQ_MODEL,

            temperature=settings.LLM_TEMPERATURE,

            max_tokens=settings.LLM_MAX_TOKENS,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        logger.info("Received response from Groq.")

        return response.choices[0].message.content
