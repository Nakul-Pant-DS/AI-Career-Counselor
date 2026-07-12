from app.core.config import settings
from app.llm.groq_provider import GroqProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        if settings.LLM_PROVIDER.lower() == "groq":
            return GroqProvider()

        raise ValueError(
            f"Unsupported LLM Provider: {settings.LLM_PROVIDER}"
        )
