from pathlib import Path

from app.core.logging import logger
from app.schemas.knowledge_document import KnowledgeDocument
from app.workflows.knowledge_workflow import KnowledgeWorkflow


class KnowledgeService:
    """
    Loads knowledge documents and indexes them.
    """

    def __init__(self):

        self.workflow = KnowledgeWorkflow()

    def ingest_text_file(
        self,
        file_path: str,
        source: str
    ):

        logger.info(f"Loading {file_path}")

        path = Path(file_path)

        content = path.read_text(
            encoding="utf-8"
        )

        document = KnowledgeDocument(

            document_name=path.name,

            source=source,

            content=content

        )

        self.workflow.ingest(document)
