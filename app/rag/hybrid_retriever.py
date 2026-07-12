from app.rag.retriever import Retriever
from app.schemas.retrieved_context import RetrievedContext
from app.schemas.vector_index import VectorIndex


class HybridRetriever:

    def __init__(self):

        self.resume = Retriever(VectorIndex.RESUME)

        self.career = Retriever(VectorIndex.CAREER)

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievedContext:

        resume = self.resume.retrieve(
            query=query,
            top_k=top_k
        )

        career = self.career.retrieve(
            query=query,
            top_k=top_k
        )

        return RetrievedContext(

            resume_chunks=resume,

            career_chunks=career,

            total_chunks=len(resume) + len(career)

        )
