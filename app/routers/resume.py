from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.resume_schema import UploadResumeResponse
from app.services.resume_service import ResumeService

from app.core.logging import logger

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post(
    "/upload",
    response_model=UploadResumeResponse
)
def upload_resume(file: UploadFile = File(...)):

    try:

        result = ResumeService.save_resume(file)

        document = result["document"]

        return UploadResumeResponse(
            message="Resume uploaded successfully.",
            filename=result["filename"],
            pages=document.pages,
            characters=document.characters,
            preview=document.preview
        )

    except ValueError as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
