from app.rag.chunker import Chunker
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore
from app.schemas.vector_index import VectorIndex
from app.utils.document_parser import DocumentParser

document = DocumentParser.extract_text(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

chunker = Chunker()

chunks = chunker.split(document.text)

embedder = EmbeddingService()

embeddings = embedder.encode(chunks)

from app.schemas.document_chunk import DocumentChunk

document_chunks = []

for i, chunk in enumerate(chunks):

    document_chunks.append(

        DocumentChunk(

            chunk_id=i,

            text=chunk,

            metadata={
                "source": "resume",
                "document_name": "nakul_resume.pdf"
            }

        )

    )
store = VectorStore(VectorIndex.RESUME)

store.add(
    embeddings,
    document_chunks
)

print("=" * 60)

print("Vectors Stored :", store.total_vectors())

print("=" * 60)
