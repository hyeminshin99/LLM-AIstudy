from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

res = llm.invoke("현재 날씨가 어떻게 되나요?")
print(res.content)