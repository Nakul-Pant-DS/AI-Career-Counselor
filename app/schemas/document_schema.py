from pydantic import BaseModel


class DocumentData(BaseModel):
    pages: int
    characters: int
    text: str
    preview: str
