class RAGPrompt:

    @staticmethod
    def build(
        question: str,
        context: str
    ) -> str:

        return f"""
You are an expert AI Career Counselor.

Answer ONLY using the information contained inside the retrieved context.

If the answer cannot be found in the context, clearly say:

"I could not find enough information in the retrieved documents."

Retrieved Context:

{context}

Question:

{question}

Answer:
"""
