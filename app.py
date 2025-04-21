import streamlit as st
from rag_engine import generate_response

st.set_page_config(page_title="🧠 Myth Buster", layout="centered")

st.title("🧠 Myth Buster")
st.subheader("Busting Myths with Evidence-Powered AI")

user_input = st.text_area("Enter a myth or urban legend you'd like to bust:", height=150)

if st.button("Bust the Myth"):
    if user_input.strip():
        with st.spinner("Analyzing myth and gathering evidence..."):
            response = generate_response(user_input)
        st.markdown("### ✅ Myth Busted!")
        st.write(response)
    else:
        st.warning("Please enter a myth to analyze.")
