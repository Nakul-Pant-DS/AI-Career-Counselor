from pydantic import BaseModel
from typing import Dict


class DocumentChunk(BaseModel):
    """
    Represents a chunk stored inside the vector database.
    """

    chunk_id: int

    text: str

    metadata: Dict = {}
