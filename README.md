## Pizza Restaurant Q&A Chatbot
This project is an AI-powered assistant designed to answer questions about a pizza restaurant using real customer reviews. It combines LangChain with Ollama to retrieve relevant reviews from a vector database and generate contextual answers using the llama3.2 language model.

## Overview
- Input: User asks a question about the restaurant.

- Processing:
  - Top 5 relevant reviews are retrieved using a Chroma vector database and mxbai-embed-large embeddings.
  - A prompt is created with the reviews and the user's question.
  - The llama3.2 model from Ollama generates a response.

- Output: A helpful answer based on real customer experiences.


## Features
- Retrieves contextually relevant reviews using vector search
- Embeds customer reviews using mxbai-embed-large via Ollama
- Generates dynamic answers using llama3.2
- Fully interactive command-line interface
- Automatically builds a vector store if one does not exist

## Project Structure
```.
├── realistic_restaurant_reviews.csv  # CSV with customer reviews
├── vector.py                         # Creates vector store and retriever
├── main.py                           # Runs the interactive chatbot
├── chroma_langchain_db/              # Auto-generated vector DB (on first run)
├── README.md                         # This file
├── requirements.txt                  # Contains the required python langchain libraries
```

## Requirements
- Python 3.8+
- Ollama installed and running locally
- Models: llama3.2 and mxbai-embed-large (available via Ollama)
- CSV file: realistic_restaurant_reviews.csv

## Python Dependencies
Install the required Python libraries:

```pip install requirements.txt``` 

OR 

```pip install langchain-core langchain-ollama langchain-chroma pandas```

## 🧩 vector.py – Vector Store Setup
This script:

1. Loads customer reviews from realistic_restaurant_reviews.csv
2. Embeds them using mxbai-embed-large
3. Stores them in a Chroma vector database (./chroma_langchain_db)
4. Creates a retriever that returns the top 5 most relevant documents

## Example review structure in CSV:
|Title|	Review|	Rating|	Date|
|-----|-------|-------|-----|
|Great Pizza|	Loved the crust and fast service. Will return!|	5 |	2024-01-15|
|Disappointing|	Waited too long, and the pizza was cold.|	2	| 2024-02-10 |

## 🤖 main.py – Interactive Chatbot
This script:
  - Loads the retriever from vector.py
  - Builds a prompt with reviews and the user's question
  - Passes the prompt to the llama3.2 model
  - Prints the AI-generated answer

## Example usage:
```python main.py```

```------------------------
Ask a question about the restaurant (type 'x' to exit): What do customers think about the pizza crust?
```
The assistant will answer using the most relevant reviews found in the database.

## ✅ First-Time Setup Notes
- On the first run, vector.py will create and persist the vector store.

- On subsequent runs, it reuses the stored data without re-embedding.



