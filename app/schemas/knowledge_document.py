from pydantic import BaseModel


class KnowledgeDocument(BaseModel):
    """
    Represents a knowledge document before chunking.
    """

    document_name: str

    source: str

    content: str
