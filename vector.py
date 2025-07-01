from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document 
import os
import pandas as pd 

# Load the CSV file containing the restaurant reviews
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Load the Embeddings model
embedding_mod = OllamaEmbeddings(model = "mxbai-embed-large")

# Define the location for the Chroma vector store
db_location = "./chroma_langchain_db" 
add_documents = not os.path.exists(db_location) # Check if the database already exists

# If the database does not exist, add documents to it
if add_documents:
    documents = []
    ids = []

    # Iterate through the DataFrame and create Document objects
    for i, row in df.iterrows():
        document = Document(
            page_content = row["Title"] + " " + row["Review"],
            metadata = {"rating": row["Rating"], "date": row["Date"]},
            id = str(i)
        )
        documents.append(document)
        ids.append(str(i))

# Create a Chroma vector store
vector_store = Chroma(
    collection_name = "restaurant_reviews",
    embedding_function=embedding_mod,
    persist_directory=db_location
)

# If the database does not exist, add documents to the vector store
if add_documents:
    # Add the documents and their IDs to the vector store
    vector_store.add_documents(documents=documents, ids=ids)


retriever = vector_store.as_retriever( # Create a retriever from the vector store
    search_kwargs={"k": 5}  # Retrieve the top 5 most relevant documents
)