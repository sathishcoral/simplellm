import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Initialize Streamlit app
st.set_page_config(page_title="Kandan - LLM Chat", layout="wide")
st.title("🤖 Kandan - Your Helpful Assistant")

# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant named Kandan.")
    ]
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm Kandan. How can I help you today?"}
    ]

# Display chat messages from session state
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
if user_input := st.chat_input("Ask me anything..."):
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Call Ollama LLM
    llm = ChatOllama(model="llama2")
    response = llm(st.session_state.chat_history)
    assistant_reply = response.content

    # Show assistant reply
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    # Update session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.session_state.chat_history.append(AIMessage(content=assistant_reply))
