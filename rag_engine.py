import cohere
from retriever import build_or_load_index, search_index

# 🔐 Set your Cohere API key here
cohere_api_key = "dLp2kuvZ7wa6JlFwFyeSt6ca4IwXYtJ4iCqsi2e7"
co = cohere.Client(cohere_api_key)

# 🔁 Load index and documents
index, chunk_store = build_or_load_index()

def generate_response(user_query):
    # 1. Retrieve relevant myth-busting chunks
    relevant_chunks = search_index(index, chunk_store, user_query)

    # 2. Combine chunks into a single context
    context = "\\n".join(relevant_chunks)

    # 3. Formulate prompt
    prompt = f"""
You are a myth-busting assistant. Based on the evidence below, respond to the following myth or question with factual information.

Evidence:
{context}

Myth/Question:
{user_query}

Answer:
"""

    # 4. Get completion from Cohere
    response = co.generate(
        model='command-xlarge',           # You can choose the appropriate model size
        prompt=prompt,            # The input prompt based on retrieved evidence
        max_tokens=300,           # Maximum tokens in the response
        temperature=0.7,          # Response creativity level
        stop_sequences=["\n"]     # To ensure the model stops at the end of the answer
    )

    # Return the answer from Cohere's response
    return response.generations[0].text.strip()
