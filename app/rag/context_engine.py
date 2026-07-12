from app.core.logging import logger
from app.schemas.retrieved_context import RetrievedContext


class ContextEngine:
    """
    Builds readable context from retrieved chunks.
    """

    @staticmethod
    def build(context: RetrievedContext):

        logger.info("Building Hybrid Context.")

        resume = ""

        for i, chunk in enumerate(context.resume_chunks, start=1):

            resume += f"""

Resume Chunk {i}
----------------------------------------

{chunk.text}

"""

        career = ""

        for i, chunk in enumerate(context.career_chunks, start=1):

            career += f"""

Career Chunk {i}
----------------------------------------

{chunk.text}

"""

        logger.info("Hybrid Context Built.")

        return {

            "resume_context": resume,

            "career_context": career

        }
