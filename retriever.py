
import os
import faiss
import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Initialize embedding model (you can replace with OpenAI if preferred)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Path to myth data
MYTH_DIR = "myth_data"
INDEX_FILE = "faiss_index.index"
CHUNK_SIZE = 100

def load_and_chunk_documents() -> List[str]:
    chunks = []
    for file_path in Path(MYTH_DIR).glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            for i in range(0, len(text), CHUNK_SIZE):
                chunk = text[i:i+CHUNK_SIZE].strip()
                if chunk:
                    chunks.append(chunk)
    return chunks

def create_faiss_index(chunks: List[str]):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings, chunks

def search_index(index, chunks, query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]

# Utility to build or reload index
def build_or_load_index():
    chunks = load_and_chunk_documents()
    index, embeddings, chunk_store = create_faiss_index(chunks)
    return index, chunk_store
