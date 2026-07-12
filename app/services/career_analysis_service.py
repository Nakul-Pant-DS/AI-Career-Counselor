from app.core.logging import logger

from app.llm.response_parser import ResponseParser
from app.prompts.career_analysis_prompt import CareerAnalysisPrompt
from app.rag.context_engine import ContextEngine
from app.rag.hybrid_retriever import HybridRetriever
from app.schemas.career_analysis import CareerAnalysis
from app.services.llm_service import LLMService


class CareerAnalysisService:
    """
    Generates an AI-powered career analysis by combining
    resume information with career knowledge.
    """

    def __init__(self):

        self.retriever = HybridRetriever()

        self.context_engine = ContextEngine()

        self.llm = LLMService()

    def analyze(
        self,
        question: str
    ) -> CareerAnalysis:

        logger.info("=" * 70)
        logger.info("STARTING CAREER ANALYSIS")
        logger.info("=" * 70)

        # --------------------------------------------------
        # Step 1 : Retrieve Context
        # --------------------------------------------------

        retrieved_context = self.retriever.retrieve(question)

        # --------------------------------------------------
        # Step 2 : Build Readable Context
        # --------------------------------------------------

        context = self.context_engine.build(
            retrieved_context
        )

        # --------------------------------------------------
        # Step 3 : Build Prompt
        # --------------------------------------------------

        prompt = CareerAnalysisPrompt.build(

            question=question,

            resume_context=context["resume_context"],

            career_context=context["career_context"]

        )

        # --------------------------------------------------
        # Step 4 : Call LLM
        # --------------------------------------------------

        response = self.llm.ask(prompt)

        # --------------------------------------------------
        # Step 5 : Parse JSON
        # --------------------------------------------------

        json_data = ResponseParser.parse(response)

        # --------------------------------------------------
        # Step 6 : Validate Output
        # --------------------------------------------------

        analysis = CareerAnalysis(**json_data)

        logger.info("Career analysis completed.")

        return analysis
