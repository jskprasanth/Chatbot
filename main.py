import os
import streamlit as st
import ollama
import time


# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with E-commerce chatbot",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Display the chatbot's title on the page
st.title("🤖 E-commerce - ChatBot")

prompt = st.chat_input("Ask")

if prompt:


    with st.chat_message("user"):
        st.write(prompt)


    with st.spinner("Thinking...."):
        result = ollama.chat(model="llama3.1",messages=[{
            "role":"user",
            "content":prompt,
        }])
        response = result["message"]["content"]
        with st.chat_message("assistant"):
            st.write(response)