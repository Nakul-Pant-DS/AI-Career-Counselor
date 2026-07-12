from pathlib import Path

from app.core.logging import logger
from app.rag.chunker import Chunker
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore
from app.schemas.document_chunk import DocumentChunk
from app.schemas.knowledge_document import KnowledgeDocument


class KnowledgeWorkflow:
    """
    Generic workflow for ingesting knowledge documents.
    """

    def __init__(self):

        self.chunker = Chunker()
        self.embedder = EmbeddingService()
        self.store = VectorStore()

    def ingest(self, document: KnowledgeDocument):

        logger.info("=" * 70)
        logger.info(f"Ingesting {document.document_name}")
        logger.info("=" * 70)

        chunks = self.chunker.split(document.content)

        embeddings = self.embedder.encode(chunks)

        documents = []

        for i, chunk in enumerate(chunks):

            documents.append(

                DocumentChunk(

                    chunk_id=i,

                    text=chunk,

                    metadata={

                        "source": document.source,

                        "document_name": document.document_name

                    }

                )

            )

        self.store.add(
            embeddings,
            documents
        )

        self.store.save()

        logger.info(
            f"{document.document_name} successfully indexed."
        )
