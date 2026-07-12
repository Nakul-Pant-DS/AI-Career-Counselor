from app.services.llm_service import LLMService

service = LLMService()

response = service.ask("Say hello in one sentence.")

print(response)
