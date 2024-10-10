import sqlite3
import src.generate_embeddings as generate_embeddings
import pickle

conn = sqlite3.connect('../output/embeddings.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS embeddings (id INTEGER PRIMARY KEY, text TEXT, embedding BLOB)''')

def store_embedding(text, embedding):
    embedding_blob = pickle.dumps(embedding)
    c.execute('INSERT INTO embeddings (text, embedding) VALUES (?, ?)', (text, embedding_blob))
    conn.commit()

if __name__ == "__main__":
    text = generate_embeddings.extract_text.extract_text_from_pdf('../data/sample.pdf')
    embedding = generate_embeddings.generate_embeddings(text)
    store_embedding(text, embedding)
