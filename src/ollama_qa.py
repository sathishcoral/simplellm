from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.set_page_config(page_title="Kandan Chatbot", layout="wide")
st.title("🤖 Sathish's Chatbot (Kandan)")

# Initialize message history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("system", "You are a wonderful assistant. Your name is Kandan.")
    ]

# Display previous messages
for role, msg in st.session_state.chat_history:
    if role != "system":  # Skip showing the system prompt
        with st.chat_message(role):
            st.markdown(msg)

# User input
if prompt := st.chat_input("Hello! What can I do for you today?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append(("user", prompt))

    # Prepare prompt dynamically using chat history
    prompt_template = ChatPromptTemplate.from_messages(st.session_state.chat_history)

    # LLM and parser setup
    llm = Ollama(model="llama2")
    output_parser = StrOutputParser()

    # Chain: prompt -> llm -> parse
    chain = prompt_template | llm | output_parser

    # Run the chain with last user query
    response = chain.invoke({"usrquery": prompt})

    # Display and store assistant reply
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append(("assistant", response))
