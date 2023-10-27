import os
import pinecone 
from langchain.vectorstores import Pinecone 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from pdf_processor import doc_preprocessing

load_dotenv()

#Get Private Keys from .env file
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY') 
PINECONE_ENV = os.getenv('PINECONE_ENV')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

def embedding_db():
    # Used the openAI embedding model
    embeddings = OpenAIEmbeddings()
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_ENV
    )
    docs_split = doc_preprocessing()
    doc_db = Pinecone.from_documents(
        docs_split, 
        embeddings, 
        index_name='ccc-text-db'
    )
    return doc_db

llm = ChatOpenAI()
doc_db = embedding_db()

def retrieve_answer(query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=doc_db.as_retriever(),
    )
    query = query
    result = qa.run(query)
    return result

def main():
    
    print("Welcome to the Climate Change Action Assistant!")

    while True:
        # Get user input from the command line
        question = input("Please ask your query (or 'exit' to quit): ")

        # Check if the user input is empty or invalid
        if not question.strip():
            print("Please enter a valid query.")
            continue

        # Check if the user wants to exit
        if question.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the answer 
        answer = retrieve_answer(question)

        # Display the answer
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()

