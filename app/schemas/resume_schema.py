from pydantic import BaseModel


class UploadResumeResponse(BaseModel):
    message: str
    filename: str
    pages: int
    characters: int
    preview: str
