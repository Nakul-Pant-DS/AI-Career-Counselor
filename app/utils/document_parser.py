import fitz
from app.core.logging import logger
from app.schemas.document_schema import DocumentData


class DocumentParser:

    @staticmethod
    def extract_text(pdf_path: str) -> dict:

        logger.info(f"Opening PDF: {pdf_path}")

        try:

            with fitz.open(pdf_path) as pdf:

                extracted_text = ""

                total_pages = len(pdf)

                for page in pdf:
                    extracted_text += page.get_text()

            logger.info("PDF text extraction completed.")

            return DocumentData(
                pages=total_pages,
                characters=len(extracted_text),
                text=extracted_text,
                preview=extracted_text[:300]
            )

        except Exception as e:

            logger.error(f"PDF Extraction Failed: {e}")

            raise
