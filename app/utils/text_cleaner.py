import re
from app.core.logging import logger


class TextCleaner:
    """
    Utility class for cleaning extracted document text
    before sending it to the LLM.
    """

    @staticmethod
    def clean(text: str) -> str:
        logger.info("Cleaning extracted text.")

        # Convert tabs to spaces
        text = text.replace("\t", " ")

        # Remove extra spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Strip leading/trailing whitespace
        text = text.strip()

        logger.info("Text cleaning completed.")

        return text
