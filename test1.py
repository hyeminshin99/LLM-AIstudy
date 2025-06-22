from dotenv import load_dotenv
import streamlit as st

load_dotenv()


from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

 
st.write("""
# 인공지능 시인
""")

poem = st.text_input("시를 입력해주세요.")

if st.button("시 작성하기"):
    with st.spinner("Wait for it...", show_time=True): #돌아가는 애니메이션 
        res = llm.invoke(poem + " 시를 작성해주세요.") #프롬프트
        st.write(res.content)