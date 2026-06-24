def build_prompt(
    context: str,
    question: str
):

    prompt = f"""
You are an expert software engineer.

Your task is to answer questions about a software repository.

Use ONLY the repository context provided below.

If the answer cannot be found in the context,
respond with:
"Information not found in the repository context."

Be concise and cite the relevant files when possible.

Repository Context:

{context}

Question:

{question}

Answer:
"""

    return prompt