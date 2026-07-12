from pydantic import BaseModel, Field


class CareerAnalysis(BaseModel):
    """
    Structured AI Career Analysis returned by the Career Analysis Service.
    """

    suitability_score: int = Field(
        ge=0,
        le=100,
        description="Overall suitability score from 0 to 100."
    )

    recommended_roles: list[str] = Field(
        default_factory=list,
        description="Roles recommended for the candidate."
    )

    strengths: list[str] = Field(
        default_factory=list,
        description="Candidate's strengths identified from the resume."
    )

    missing_skills: list[str] = Field(
        default_factory=list,
        description="Important skills missing for the target role."
    )

    learning_roadmap: list[str] = Field(
        default_factory=list,
        description="Suggested learning roadmap."
    )

    summary: str = Field(
        description="Overall career recommendation summary."
    )
