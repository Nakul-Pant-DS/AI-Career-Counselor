from app.core.logging import logger
from app.rag.chunker import Chunker
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore
from app.schemas.document_chunk import DocumentChunk
from app.schemas.ingestion_request import IngestionRequest


class DocumentIngestionService:
    """
    Generic document ingestion pipeline.

    Supports ingestion of any document into any vector index.
    """

    def __init__(self):

        self.chunker = Chunker()
        self.embedder = EmbeddingService()

    def ingest(self, request: IngestionRequest):

        logger.info("=" * 70)
        logger.info(f"Ingesting {request.document_name}")
        logger.info("=" * 70)

        # -------------------------------------------------
        # Step 1 : Chunking
        # -------------------------------------------------

        logger.info("STEP 1 - Chunking started")

        chunks = self.chunker.split(request.content)

        logger.info(f"STEP 1 COMPLETE : {len(chunks)} chunks")

        logger.info(f"Created {len(chunks)} chunks.")

        # -------------------------------------------------
        # Step 2 : Embeddings
        # -------------------------------------------------

        logger.info("STEP 2 - Generating embeddings")

        embeddings = self.embedder.encode(chunks)

        logger.info("STEP 2 COMPLETE")

        # -------------------------------------------------
        # Step 3 : Create DocumentChunk objects
        # -------------------------------------------------

        documents = []

        for i, chunk in enumerate(chunks):

            documents.append(

                DocumentChunk(

                    chunk_id=i,

                    text=chunk,

                    metadata={
                        "source": request.source,
                        "document_name": request.document_name
                    }

                )

            )

        # -------------------------------------------------
        # Step 4 : Store
        # -------------------------------------------------

        logger.info("STEP 3 - Loading vector store")

        store = VectorStore(request.target_index)

        logger.info("STEP 3 COMPLETE")

        logger.info("STEP 4 - Writing FAISS")

        store.append(
            embeddings,
            documents
        )

        logger.info("STEP 4 COMPLETE")

        logger.info("Document ingestion completed.")
