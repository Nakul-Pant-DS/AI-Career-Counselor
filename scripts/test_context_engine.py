from app.rag.context_engine import ContextEngine
from app.rag.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

context = retriever.retrieve(

    "What skills are required to become an AI Engineer?"

)

result = ContextEngine.build(context)

print("=" * 80)
print("RESUME CONTEXT")
print("=" * 80)

print(result["resume_context"][:1000])

print()

print("=" * 80)
print("CAREER CONTEXT")
print("=" * 80)

print(result["career_context"][:1000])
