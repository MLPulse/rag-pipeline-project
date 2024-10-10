from ollama import Ollama
import src.query_retrieval as query_retrieval

llm = Ollama(model='command-r')

def generate_response(chunks):
    prompt = "\n".join(chunks)
    response = llm.complete(prompt=prompt)
    return response

if __name__ == "__main__":
    query = "What is the main topic of the document?"
    chunks = query_retrieval.retrieve_relevant_chunks(query)
    response = generate_response(chunks)
    print(response)
