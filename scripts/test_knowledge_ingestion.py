from app.services.knowledge_service import KnowledgeService

service = KnowledgeService()

service.ingest_text_file(
    "data/career_docs/ai_engineer.txt",
    source="career_docs"
)

print("\nKnowledge document indexed successfully.")
