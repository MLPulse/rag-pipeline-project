import sqlite3
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from ollama import Ollama

llm = Ollama(model='command-r')

conn = sqlite3.connect('../output/embeddings.db')
c = conn.cursor()

def retrieve_relevant_chunks(query, top_n=3):
    # Generate embedding for the query
    query_embedding = llm.embed(query)['embedding']

    # Retrieve all stored embeddings from the database
    c.execute('SELECT id, text, embedding FROM embeddings')
    rows = c.fetchall()

    # Calculate cosine similarity between query and stored embeddings
    similarities = []
    for row in rows:
        stored_embedding = pickle.loads(row[2])
        similarity = cosine_similarity([query_embedding], [stored_embedding])[0][0]
        similarities.append((row[0], row[1], similarity))

    # Sort by similarity and return the top_n results
    sorted_similarities = sorted(similarities, key=lambda x: x[2], reverse=True)
    top_chunks = [row[1] for row in sorted_similarities[:top_n]]

    return top_chunks

if __name__ == "__main__":
    query = "What is the main topic of the document?"
    chunks = retrieve_relevant_chunks(query)
    print(chunks)
