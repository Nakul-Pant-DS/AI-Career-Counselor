from app.utils.document_parser import DocumentParser
from app.rag.chunker import Chunker
from app.rag.embedding_service import EmbeddingService

document = DocumentParser.extract_text(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

chunker = Chunker()

chunks = chunker.split(document.text)

embedder = EmbeddingService()

vectors = embedder.encode(chunks)

print("=" * 60)

print("Number of Chunks :", len(chunks))

print("Embedding Shape  :", vectors.shape)

print("First Vector (first 10 values):")

print(vectors[0][:10])

print("=" * 60)
