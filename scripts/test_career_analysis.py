from app.services.career_analysis_service import CareerAnalysisService

service = CareerAnalysisService()

result = service.analyze(

    """
    Based on my resume,

    am I suitable for an AI Engineer role?

    Explain in detail.
    """

)

print("=" * 80)
print("CAREER ANALYSIS")
print("=" * 80)

print(result)
