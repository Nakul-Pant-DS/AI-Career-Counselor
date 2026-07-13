from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from app.core.logging import logger
from app.utils.document_parser import DocumentParser

from app.services.resume_extractor import ResumeExtractor
from app.services.document_ingestion_service import DocumentIngestionService

from app.schemas.ingestion_request import IngestionRequest
from app.schemas.vector_index import VectorIndex

UPLOAD_FOLDER = Path("data/resumes")


class ResumeService:

    @staticmethod
    def save_resume(file: UploadFile):

        logger.info(f"Uploading file: {file.filename}")

        # -------------------------------------------------
        # Validate file
        # -------------------------------------------------

        if not file.filename.lower().endswith(".pdf"):

            logger.warning(f"Rejected file: {file.filename}")

            raise ValueError("Only PDF files are allowed.")

        # -------------------------------------------------
        # Save file
        # -------------------------------------------------

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        unique_filename = f"{uuid4().hex}.pdf"

        file_path = UPLOAD_FOLDER / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"Resume saved successfully: {unique_filename}")

        # -------------------------------------------------
        # Parse PDF
        # -------------------------------------------------

        document = DocumentParser.extract_text(str(file_path))

        # -------------------------------------------------
        # Extract structured resume information
        # -------------------------------------------------

        extractor = ResumeExtractor()

        resume = extractor.extract(document.text)

        logger.info("Resume extraction completed.")

        # -------------------------------------------------
        # Ingest into Resume Vector Database
        # -------------------------------------------------

        #ingestion_request = IngestionRequest(

            #content=document.text,

            #document_name=file.filename,

            #source="resume",

            #target_index=VectorIndex.RESUME

        #)

        #ingestion_service = DocumentIngestionService()

        #ingestion_service.ingest(ingestion_request)

        logger.info("Resume successfully indexed.")

        # -------------------------------------------------
        # Return response
        # -------------------------------------------------

        return {

            "filename": unique_filename,

            "document": document,

            "resume": resume

        }
