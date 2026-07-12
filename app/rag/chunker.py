from typing import List

from app.core.logging import logger

from app.core.config import settings


class Chunker:
    """
    Splits text into overlapping chunks for RAG.
    """

    def __init__(
        self,
        chunk_size: int | None = None,
        overlap: int | None = None
    ):

        self.chunk_size = (
            chunk_size
            if chunk_size is not None
            else settings.CHUNK_SIZE
        )

        self.overlap = (
            overlap
            if overlap is not None
            else settings.CHUNK_OVERLAP
        )

    def split(self, text: str) -> List[str]:

        logger.info("Creating text chunks.")

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        logger.info(
            f"Created {len(chunks)} chunks."
        )

        return chunks
