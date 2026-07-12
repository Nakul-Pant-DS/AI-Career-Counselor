from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from app.core.logging import logger
from app.utils.document_parser import DocumentParser

UPLOAD_FOLDER = Path("data/resumes")


class ResumeService:

    @staticmethod
    def save_resume(file: UploadFile):

        logger.info(f"Uploading file: {file.filename}")

        if not file.filename.lower().endswith(".pdf"):

            logger.warning(f"Rejected file: {file.filename}")

            raise ValueError("Only PDF files are allowed.")

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        unique_filename = f"{uuid4().hex}.pdf"

        file_path = UPLOAD_FOLDER / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"Resume saved successfully: {unique_filename}")

        # Extract text immediately after saving
        document = DocumentParser.extract_text(str(file_path))

        return {
            "filename": unique_filename,
            "document": document
        }
