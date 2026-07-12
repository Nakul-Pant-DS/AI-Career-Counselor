from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.core.logging import logger


class EmbeddingService:
    """
    Generates vector embeddings for text chunks.
    """

    def __init__(self):

        logger.info(
            f"Loading embedding model: {settings.EMBEDDING_MODEL}"
        )

        from app.rag.model_registry import ModelRegistry

        self.model = ModelRegistry.embedding_model()
        

    def encode(self, texts: list[str]):

        logger.info(
            f"Generating embeddings for {len(texts)} chunks."
        )

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        logger.info(
            f"Embedding dimension: {embeddings.shape[1]}"
        )

        return embeddings
