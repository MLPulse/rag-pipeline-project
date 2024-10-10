from langchain import PromptTemplate
from ollama import Ollama
import src.query_retrieval as query_retrieval

llm = Ollama(model='command-r')

def generate_response(chunks, query):
    # Define a prompt template using LangChain
    prompt_template = PromptTemplate(
        input_variables=["context", "query"],
        template="""
        You are an expert assistant. 
        Based on the following information:\n{context}\n\n
        Answer the following query:\n{query}
        """
    )
    
    # Create the prompt using the template
    prompt = prompt_template.format(context="\n".join(chunks), query=query)
    
    # Generate response using the LLM
    response = llm.complete(prompt=prompt)
    return response

if __name__ == "__main__":
    query = "What is the main topic of the document?"
    chunks = query_retrieval.retrieve_relevant_chunks(query)
    response = generate_response(chunks, query)
    print(response)
