from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("Sathish's Chatbot")
input_txt = st.text_input("Hello! What can i do for you today?")

# defining Prompt. User question and answer
prompt = ChatPromptTemplate.from_messages(
    [("system","You are wonderful assistant. Your name is Kandan"),
     ("user","user question here: {usrquery}")
    ])

# defining LLM model name
llm = Ollama(model="llama2")

output_parser = StrOutputParser()

# chain - joining prompt + llm + output parser like a pipe/chain
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"usrquery":input_txt}))