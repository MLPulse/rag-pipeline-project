# Retrieval-Augmented Generation (RAG) Pipeline

## Description

This repository contains a pipeline for answering queries over PDF documents using embeddings. The project utilizes Ollama for 
embedding generation, LangChain for retrieval, SQLite for embedding storage, and a locally hosted Command-R LLM for response 
generation. The project is designed to facilitate efficient query-answering over large PDF documents.

## Folder Structure and Modules

The project folder structure and corresponding modules are organized as follows:

```bash

rag_pipeline_project/
├── README.md                   # Project documentation
├── requirements.txt            # List of required Python dependencies
├── main.py                     # Main execution script to run the complete workflow
├── .gitignore                  # Specifies files and folders to ignore in Git
├── data/                       # Contains raw data (PDF files)
│   └── sample.pdf
│
├── output/                     # Directory for output data
│   └── embeddings.db
│
└──  src/                       # Source code directory
    ├── extract_text.py         # Extracts text from PDF files using PyPDF2
    ├── generate_embeddings.py  # Generates embeddings for extracted text using Ollama
    ├── store_embeddings.py     # Stores generated embeddings in SQLite
    ├── query_retrieval.py      # Retrieves relevant text chunks using cosine similarity
    ├── generate_response.py    # Generates responses using the locally hosted Command-R LLM
    └── rag_pipeline_demo.ipynb # Jupyter notebook to demonstrate and test the RAG pipeline interactively
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Ollama and Command-R LLM installed locally

## Usage

### Running the Pipeline

1. Prepare Your Data

Place your PDF files in the data/ folder.

2. Run the Pipeline
Execute main.py to run the entire RAG pipeline:
```bash
python main.py
```
By default, it processes the sample.pdf and responds to the sample query.

3. Interactive Testing
   
Alternatively, use the Jupyter notebook for step-by-step interaction:
```bash
jupyter notebook src/rag_pipeline_demo.ipynb
```
### Main Script (main.py)

This script ties together all the individual components of the RAG pipeline:

- Extracts text from PDFs
- Generates embeddings
- Stores embeddings in SQLite
- Retrieves relevant text chunks based on a query
- Generates responses using Command-R LLM

## Dependencies (requirements.txt)
```bash
PyPDF2
ollama
sqlite3
langchain
numpy
scikit-learn
jupyter
```

