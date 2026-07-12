from app.utils.document_parser import DocumentParser
from app.services.resume_extractor import ResumeExtractor

document = DocumentParser.extract_text(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

extractor = ResumeExtractor()

resume = extractor.extract(document.text)

print("=" * 80)

print(resume)

print("=" * 80)
