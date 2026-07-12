from pydantic import BaseModel


class CareerAnalysisRequest(BaseModel):
    question: str
