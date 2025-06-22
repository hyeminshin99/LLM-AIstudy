import streamlit as st
import openai
import os
from dotenv import load_dotenv

from openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv() # .env 파일로드
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI 감성 챗봇")
user_input = st.text_input("메시지 입력:")

if st.button("대화하기"):
    if user_input:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("AI:", response.choices[0].message.content)
