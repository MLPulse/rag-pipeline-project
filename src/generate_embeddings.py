from sentence_transformers import SentenceTransformer
import src.extract_text as extract_text

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text):
    embedding = model.encode(text)
    return embedding

if __name__ == "__main__":
    text = extract_text.extract_text_from_pdf('../data/sample.pdf')
    embedding = generate_embeddings(text)
    print(embedding)
