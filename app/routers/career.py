from fastapi import APIRouter, HTTPException

from app.schemas.career_request import CareerAnalysisRequest
from app.schemas.career_analysis import CareerAnalysis

from app.services.career_analysis_service import CareerAnalysisService

from app.core.logging import logger

router = APIRouter(
    tags=["Career Analysis"]
)


@router.post(
    "/career-analysis",
    response_model=CareerAnalysis
)
def analyze(request: CareerAnalysisRequest):

    try:

        service = CareerAnalysisService()

        result = service.analyze(
            request.question
        )

        return result

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
