from app.core.logging import logger


class CareerAnalysisPrompt:
    """
    Builds the prompt used by the Career Analysis Service.
    """

    @staticmethod
    def build(
        question: str,
        resume_context: str,
        career_context: str
    ) -> str:

        logger.info("Building Career Analysis Prompt.")

        prompt = f"""
You are an expert AI Career Counselor.

You have been provided with two sources of information:

1. Candidate Resume
2. Career Knowledge Base

Your task is to compare the candidate's resume against the career requirements
and provide an objective analysis.

IMPORTANT RULES:

- Use ONLY the information provided below.
- Do NOT invent skills or experience.
- If information is missing, mention it explicitly.
- Return ONLY valid JSON.
- Do NOT include markdown.
- Do NOT include explanation before or after the JSON.

Return JSON in the following format:

{{
    "suitability_score": 0,
    "recommended_roles": [],
    "strengths": [],
    "missing_skills": [],
    "learning_roadmap": [],
    "summary": ""
}}

------------------------------------------------------------
CANDIDATE RESUME
------------------------------------------------------------

{resume_context}

------------------------------------------------------------
CAREER KNOWLEDGE
------------------------------------------------------------

{career_context}

------------------------------------------------------------
QUESTION
------------------------------------------------------------

{question}

Remember:

- suitability_score must be between 0 and 100.
- recommended_roles should contain 3-5 suitable job roles.
- strengths should list the candidate's strongest technical skills.
- missing_skills should contain skills required by the target role but not evident in the resume.
- learning_roadmap should contain practical learning steps in logical order.
- summary should be a concise career recommendation (100-150 words).

Return ONLY the JSON object.
"""

        logger.info("Career Analysis Prompt Built.")

        return prompt
