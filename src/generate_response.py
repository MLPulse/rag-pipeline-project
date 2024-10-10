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
    try:
        response = llm.complete(prompt=prompt)
    except Exception as e:
        print(f"An error occurred while generating the response: {e}")
        response = ""
    return response
