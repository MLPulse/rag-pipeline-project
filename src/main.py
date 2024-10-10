from src.extract_text import extract_text_from_pdf
from src.generate_embeddings import generate_embeddings
from src.store_embeddings import store_embedding
from src.query_retrieval import retrieve_relevant_chunks
from src.generate_response import generate_response

def main(pdf_path, query):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Generate and store embeddings
    embedding = generate_embeddings(text)
    store_embedding(text, embedding)

    # Retrieve relevant chunks
    chunks = retrieve_relevant_chunks(query)
    
    # Generate response
    response = generate_response(chunks, query)
    print(response)

if __name__ == "__main__":
    pdf_path = 'data/sample.pdf'
    query = "What is the main topic of the document?"
    main(pdf_path, query)
