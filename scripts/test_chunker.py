from app.utils.document_parser import DocumentParser
from app.rag.chunker import Chunker

document = DocumentParser.extract_text(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

chunker = Chunker()

chunks = chunker.split(document.text)

print("=" * 50)

print("Total Chunks:", len(chunks))

print("=" * 50)

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}\n")

    print(chunk[:250])

    print("-" * 40)
