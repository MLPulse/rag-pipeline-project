from sentence_transformers import SentenceTransformer
import src.extract_text as extract_text

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text):
    embedding = model.encode(text)
    return embedding
