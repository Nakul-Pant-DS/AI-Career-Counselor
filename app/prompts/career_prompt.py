class CareerPrompt:

    @staticmethod
    def build(
        question: str,
        resume_context: str,
        career_context: str
    ) -> str:

        return f"""
You are an AI Career Counselor.

You have access to:

1. Candidate Resume
2. Career Knowledge

Compare both.

Use ONLY the provided information.

Resume

{resume_context}

Career Knowledge

{career_context}

Question

{question}

Provide:

1. Suitability
2. Missing Skills
3. Recommendations
4. Learning Path
"""
