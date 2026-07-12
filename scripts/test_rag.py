from app.services.rag_service import RAGService

rag = RAGService()

question = """
Based on my resume,

what AI / Data Science roles am I most suitable for?

Explain why.
"""

answer = rag.ask(question)

print("\n")

print("=" * 100)

print("QUESTION")

print("=" * 100)

print(question)

print("\n")

print("=" * 100)

print("GROUNDED AI ANSWER")

print("=" * 100)

print(answer)

print("=" * 100)
