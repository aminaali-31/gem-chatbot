import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=key)
model = "gemini-3-flash-preview"
def response_generator(prompt):
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = prompt
    ):
        yield chunk.text


st.title("ChatBot")
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


if prompt := st.chat_input("What's up"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        'role':"user",
        'content':prompt
        })

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))

    st.session_state.messages.append({
        'role':'assistant',
        'content':response
    })