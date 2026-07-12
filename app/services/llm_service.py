from app.llm.provider_factory import ProviderFactory
from app.core.logging import logger


class LLMService:
    """
    Enterprise LLM Service.

    Responsibilities
    ----------------
    1. Communicate with the configured LLM provider.
    2. Keep provider-specific implementation hidden.
    3. Provide a simple interface for the rest of the application.
    """

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def ask(self, prompt: str) -> str:
        """
        Sends a prompt to the configured LLM and returns the response.
        """

        logger.info("Sending request to LLM.")

        response = self.provider.generate(prompt)

        logger.info("LLM response received.")

        return response

    # ---------------------------------------------------------
    # Backward-compatible alias
    # ---------------------------------------------------------

    def generate(self, prompt: str) -> str:
        """
        Alias for ask().

        Allows other services (like RAGService) to use
        generate() without breaking older code.
        """

        return self.ask(prompt)
