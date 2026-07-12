import json


def build_resume_prompt(resume_text: str) -> str:
    """
    Builds a structured prompt for resume information extraction.
    """

    schema = {
        "name": "",
        "email": "",
        "phone": "",
        "summary": "",
        "skills": [],
        "certifications": [],
        "experience": [
            {
                "company": "",
                "role": "",
                "duration": ""
            }
        ],
        "education": [
            {
                "degree": "",
                "institution": "",
                "year": ""
            }
        ],
        "projects": [
            {
                "title": "",
                "description": "",
                "technologies": []
            }
        ]
    }

    return f"""
You are an expert Resume Parsing AI.

Your task is to extract structured information from the resume.

IMPORTANT RULES

1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT explain anything.
4. Do NOT wrap JSON inside ``` blocks.
5. Missing fields should be null or empty lists.

JSON FORMAT

{json.dumps(schema, indent=4)}

Resume

{resume_text}
"""
