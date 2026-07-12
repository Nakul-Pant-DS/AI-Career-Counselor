from app.rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What machine learning skills does Nakul have?",
    top_k=3
)

print("=" * 80)

for i, chunk in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 80)

    print(chunk.text)

    print("\nMetadata:")

    print(chunk.metadata)

print("=" * 80)
