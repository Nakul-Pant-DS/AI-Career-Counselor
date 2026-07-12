from app.core.logging import logger
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore
from app.schemas.document_chunk import DocumentChunk
from app.schemas.vector_index import VectorIndex


class Retriever:
    """
    Enterprise Semantic Retriever.

    Responsible for:
    ----------------
    1. Loading the appropriate vector index.
    2. Converting the user query into an embedding.
    3. Performing semantic similarity search.
    """

    def __init__(
        self,
        index_name: VectorIndex = VectorIndex.RESUME
    ):

        self.embedder = EmbeddingService()

        self.vector_store = VectorStore(index_name)

        self.vector_store.load()

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> list[DocumentChunk]:

        logger.info(
            f"Retrieving context for query: {query}"
        )

        query_embedding = self.embedder.encode(
            [query]
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        logger.info(
            f"Retrieved {len(results)} chunks."
        )

        return results
