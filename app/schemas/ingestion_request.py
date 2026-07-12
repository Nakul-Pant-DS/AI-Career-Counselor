from pydantic import BaseModel

from app.schemas.vector_index import VectorIndex


class IngestionRequest(BaseModel):
    """
    Represents a document to be ingested into a vector index.
    """

    document_name: str

    source: str

    content: str

    target_index: VectorIndex
