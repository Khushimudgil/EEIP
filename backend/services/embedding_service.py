import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_embedding(text):

    if isinstance(text, list):
        embeddings = []

        for item in text:
            result = genai.embed_content(
                model="models/embedding-001",
                content=item,
                task_type="retrieval_document"
            )

            embeddings.append(result["embedding"])

        return embeddings

    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_query"
    )

    return result["embedding"]