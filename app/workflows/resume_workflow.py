from app.core.logging import logger
from app.utils.document_parser import DocumentParser
from app.services.resume_extractor import ResumeExtractor
from app.schemas.resume_data import ResumeData


class ResumeWorkflow:
    """
    Orchestrates the complete resume processing pipeline.
    """

    def __init__(self):

        self.extractor = ResumeExtractor()

    def execute(self, pdf_path: str) -> ResumeData:

        logger.info("=" * 60)
        logger.info("STARTING RESUME WORKFLOW")
        logger.info("=" * 60)

        # Step 1
        logger.info("Step 1 : Parse PDF")

        document = DocumentParser.extract_text(pdf_path)

        # Step 2
        logger.info("Step 2 : Extract Resume Information")

        resume = self.extractor.extract(document.text)

        logger.info("Resume workflow completed successfully.")

        logger.info("=" * 60)

        return resume
