import time

from app.core.logging import logger
from app.prompts.rag_prompt import RAGPrompt
from app.rag.retriever import Retriever
from app.services.llm_service import LLMService
from app.utils.context_builder import ContextBuilder


class RAGService:
    """
    Enterprise Retrieval-Augmented Generation Service.

    Pipeline

    User Question
            ↓
       Semantic Retrieval
            ↓
        Context Builder
            ↓
         Prompt Builder
            ↓
          LLM Service
            ↓
      Grounded AI Response
    """

    def __init__(self):

        self.retriever = Retriever()

        self.llm = LLMService()

    def ask(
        self,
        question: str,
        top_k: int = 3
    ) -> str:

        logger.info("=" * 70)
        logger.info("STARTING RAG PIPELINE")
        logger.info("=" * 70)

        start_time = time.perf_counter()

        try:

            # --------------------------------------------------
            # Step 1 : Semantic Retrieval
            # --------------------------------------------------

            logger.info("Step 1 : Retrieving relevant context.")

            chunks = self.retriever.retrieve(
                question,
                top_k
            )

            # --------------------------------------------------
            # Step 2 : Build Context
            # --------------------------------------------------

            logger.info("Step 2 : Building context.")

            context = ContextBuilder.build(chunks)

            # --------------------------------------------------
            # Step 3 : Build Prompt
            # --------------------------------------------------

            logger.info("Step 3 : Building RAG prompt.")

            prompt = RAGPrompt.build(
                question=question,
                context=context
            )

            # --------------------------------------------------
            # Step 4 : LLM
            # --------------------------------------------------

            logger.info("Step 4 : Calling LLM.")

            answer = self.llm.ask(prompt)

            elapsed = round(
                time.perf_counter() - start_time,
                2
            )

            logger.info("=" * 70)
            logger.info("RAG PIPELINE COMPLETED")
            logger.info(f"Execution Time : {elapsed} sec")
            logger.info("=" * 70)

            return answer

        except Exception as e:

            logger.exception(
                f"RAG Pipeline Failed : {e}"
            )

            raise
