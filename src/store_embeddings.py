import sqlite3
import src.generate_embeddings as generate_embeddings
import pickle

conn = sqlite3.connect('../output/embeddings.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS embeddings (id INTEGER PRIMARY KEY, text TEXT, embedding BLOB)''')

def store_embedding(text, embedding):
    try:
        embedding_blob = pickle.dumps(embedding)
        c.execute('INSERT INTO embeddings (text, embedding) VALUES (?, ?)', (text, embedding_blob))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while storing the embedding: {e}")
