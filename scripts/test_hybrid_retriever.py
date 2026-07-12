from app.rag.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

results = retriever.retrieve(
    "What skills are required to become an AI Engineer?"
)

print("=" * 70)
print("RESUME RESULTS")
print("=" * 70)

for chunk in results["resume"]:
    print(chunk.metadata["document_name"])

print("\n")

print("=" * 70)
print("CAREER RESULTS")
print("=" * 70)

for chunk in results["career"]:
    print(chunk.metadata["document_name"])
