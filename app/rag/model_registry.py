from sentence_transformers import SentenceTransformer

from app.core.config import settings


class ModelRegistry:
    """
    Loads AI models only once.
    """

    _embedding_model = None

    @classmethod
    def embedding_model(cls):

        if cls._embedding_model is None:

            cls._embedding_model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return cls._embedding_model
