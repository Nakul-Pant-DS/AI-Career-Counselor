from pydantic import BaseModel

from app.schemas.document_chunk import DocumentChunk


class RetrievedContext(BaseModel):
    """
    Structured context returned by HybridRetriever.
    """

    resume_chunks: list[DocumentChunk]

    career_chunks: list[DocumentChunk]

    total_chunks: int
