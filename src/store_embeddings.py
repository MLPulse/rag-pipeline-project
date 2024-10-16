import sqlite3
import src.generate_embeddings as generate_embeddings
import pickle

import os
# Ensure the output directory exists
output_dir = '../output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Proceed with database connection
conn = sqlite3.connect(os.path.join(output_dir, 'embeddings.db'))

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS embeddings 
             (id INTEGER PRIMARY KEY, text TEXT, embedding BLOB)''')

def store_embedding(text, embedding):
    try:
        embedding_blob = pickle.dumps(embedding)
        c.execute('INSERT INTO embeddings (text, embedding) VALUES (?, ?)', (text, embedding_blob))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while storing the embedding: {e}")
