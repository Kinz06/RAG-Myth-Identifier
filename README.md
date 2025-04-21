#  Myth Identifier – A RAG-Powered Urban Legend Analyzer

> **"Separate fact from fiction with the power of Retrieval-Augmented Generation."**

**Myth Identifier** is a lightweight AI application that uses Retrieval-Augmented Generation (RAG) to investigate and respond to urban legends, myths, and commonly debated claims. This app intelligently fetches evidence from a curated document base and leverages the power of **Cohere’s LLM** to generate factual, easy-to-understand responses.

---

##  Features

-  **Ask Anything**: Input any myth, urban legend, or questionable claim.
-  **Smart Retrieval**: Uses FAISS and LangChain to fetch the most relevant sources.
-  **AI-Powered Response**: Summarizes evidence and answers using Cohere's Command R model.
-  **User-Friendly Interface**: Simple and clean UI built with Streamlit.

---

##  Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **RAG Engine**: LangChain  
- **Vector Store**: FAISS  
- **Embeddings & LLM**: Cohere API  
- **Data Source**: Local `.txt` documents  

---

##  How It Works

1. User enters a myth or statement.
2. The system retrieves relevant info using FAISS and LangChain.
3. The retrieved context is sent to Cohere’s LLM to generate a well-informed response.
4. The final answer is displayed clearly on the app interface.

---

