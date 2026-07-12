from app.rag.vector_store import VectorStore
from app.schemas.vector_index import VectorIndex

store = VectorStore(VectorIndex.RESUME)

store.load()

print("=" * 60)

print("Total Vectors :", store.total_vectors())

print("Documents Loaded :", len(store.documents))

print("=" * 60)

print("\nFirst Chunk\n")

print(store.documents[0])
