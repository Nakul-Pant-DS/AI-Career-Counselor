from app.utils.document_parser import DocumentParser

result = DocumentParser.extract_text(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

print("=" * 50)
print("Pages:", result["pages"])
print("Characters:", result["characters"])
print("=" * 50)
print(result["preview"])
