import fitz
from app.core.logging import logger
from app.schemas.document_schema import DocumentData
from app.utils.text_cleaner import TextCleaner


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
            clean_text = TextCleaner.clean(extracted_text)

            return DocumentData(
                pages=total_pages,
                characters=len(clean_text),
                text=clean_text,
                preview=clean_text[:300]
            )

        except Exception as e:

            logger.error(f"PDF Extraction Failed: {e}")

            raise
