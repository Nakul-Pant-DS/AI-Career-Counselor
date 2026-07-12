from app.core.logging import logger
from app.schemas.document_chunk import DocumentChunk


class ContextBuilder:
    """
    Builds formatted context from retrieved document chunks.
    """

    @staticmethod
    def build(chunks: list[DocumentChunk]) -> str:

        logger.info("Building RAG context.")

        context = []

        context.append("=" * 60)
        context.append("RETRIEVED CONTEXT")
        context.append("=" * 60)

        for i, chunk in enumerate(chunks, start=1):

            context.append(f"\nChunk {i}")
            context.append("-" * 60)
            context.append(chunk.text.strip())

        context.append("\n" + "=" * 60)

        logger.info("Context successfully built.")

        return "\n".join(context)
