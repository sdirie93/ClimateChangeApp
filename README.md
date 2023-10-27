# Climate Change Action Assistant

## Overview
The Climate Change Action Assistant is an app that can give insights into current Climate Change Legislation and progress. The assistant can summarise and answer questions sourced from the Climate Change Consortium's publications.

## Features
**Document Processing** : Directly loads and processes PDF publications.
**Query-Based Summaries**: Users can ask specific questions and get response based their queries.
**Vector-Based Search**: Efficient and semantic search mechanism thanks to embedding the documents into vectors.

## Technologies Used
**Langchain**: For document loading, text splitting, embedding through OpenAI and interaction with the chat model.
**Pinecone**: Used as the vector database to store and retrieve embedded document chunks efficiently.
**OpenAI**: Provides the underlying Large Language Model (LLM) for generating coherent responses.

## How to Use
Once set up, launch the terminal-based interface.
You'll be greeted with a prompt asking for your query related to climate change.
Input your question, and the assistant will retrieve a relevant answer.
To exit, type 'exit' at the prompt.

## Future Enhancements
A web-based user interface for broader accessibility.
