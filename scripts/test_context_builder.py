from app.rag.retriever import Retriever
from app.utils.context_builder import ContextBuilder
from app.prompts.rag_prompt import RAGPrompt

retriever = Retriever()

chunks = retriever.retrieve(
    "What machine learning skills does Nakul have?"
)

context = ContextBuilder.build(chunks)

prompt = RAGPrompt.build(
    question="What machine learning skills does Nakul have?",
    context=context
)

print("=" * 80)
print(prompt)
print("=" * 80)
