from pathlib import Path

from app.schemas.ingestion_request import IngestionRequest
from app.schemas.vector_index import VectorIndex
from app.services.document_ingestion_service import DocumentIngestionService
from app.rag.vector_store import VectorStore

service = DocumentIngestionService()

# ----------------------------------------------------
# AI Engineer
# ----------------------------------------------------

content = Path(
    "data/career_docs/ai_engineer.txt"
).read_text(
    encoding="utf-8"
)

request = IngestionRequest(
    document_name="ai_engineer.txt",
    source="career_docs",
    content=content,
    target_index=VectorIndex.CAREER
)

service.ingest(request)

# ----------------------------------------------------
# Data Scientist
# ----------------------------------------------------

content = Path(
    "data/career_docs/data_scientist.txt"
).read_text(
    encoding="utf-8"
)

request = IngestionRequest(
    document_name="data_scientist.txt",
    source="career_docs",
    content=content,
    target_index=VectorIndex.CAREER
)

service.ingest(request)

# ----------------------------------------------------
# Verify
# ----------------------------------------------------

store = VectorStore(VectorIndex.CAREER)

store.load()

print("\n")
print("=" * 60)
print("CAREER INDEX")
print("=" * 60)

print("Total Vectors :", store.total_vectors())
print("Documents :", len(store.documents))

print("\nDocuments Found:\n")

unique_docs = sorted(
    {
        doc.metadata["document_name"]
        for doc in store.documents
    }
)

for doc in unique_docs:
    print("-", doc)

print("=" * 60)
