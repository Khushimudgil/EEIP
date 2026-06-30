from sentence_transformers import SentenceTransformer

model = None

def get_model():
    global model

    if model is None:
        print("Loading embedding model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Embedding model loaded")

    return model


def generate_embedding(text):

    model = get_model()

    if isinstance(text, list):
        embeddings = model.encode(text)
        return embeddings.tolist()

    embedding = model.encode(text)
    return embedding.tolist()