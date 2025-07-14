import streamlit as st
import openai

st.title("🧠 GPT Chatbot")

openai.api_key = st.secrets["OPENAI_API_KEY"]  # or use st.text_input to input manually
st.write("API Key loaded:", openai.api_key[:5] + "*****")