from ollama import Ollama
import src.extract_text as extract_text

llm = Ollama(model='command-r')

def generate_embeddings(text):
    response = llm.embed(text)
    return response['embedding']

if __name__ == "__main__":
    text = extract_text.extract_text_from_pdf('../data/sample.pdf')
    embedding = generate_embeddings(text)
    print(embedding)
