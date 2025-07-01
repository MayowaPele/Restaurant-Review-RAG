from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an assistannt in answering questions about a pizza restaurant

Here are some important reviews from customers: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template) # Create a prompt template using the template created above
chain = prompt | model # Create a chain combining the prompt and the model

# Allow the user to ask questions about the restaurant until they type 'x' to exit
while True:
    print("\n\n------------------------")
    question = input("Ask a question about the restaurant (type 'x' to exit): ")
    print("\n\n")
    if question.lower() == 'x':
        break

    # Retrieve relevant reviews from the vector store
    reviews = retriever.invoke(question)

    # Invoke the chain with the retrieved reviews and the user's question
    result = chain.invoke({"reviews": reviews, "question": question}) 
    print(result) # Print the result of the chain invocation

