from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)

def embed_text(text: str):
    return model.encode([text])[0]