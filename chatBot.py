import streamlit as st
import openai
from helpers.functions.get_QA_pool import get_QA_pool
from helpers.functions.get_answer_from_data import get_answer_from_data
from helpers.functions.get_answer_from_openai import get_answer_from_openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Instructions for the AI
max_tokens, temperature, context = 70, 0, "Data Science"
message_to_ai = f'''Answer in question's language, 
                   end with a related emoji,
                   stick to {context} context
                   within max {max_tokens} tokens,
                   10 tokens if out of context.'''

# Load questions and answers
questions, answers = get_QA_pool()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": message_to_ai}]

# Chatbot UI
st.header("Chat with Techpro Education 🤖")

# 1- gets user input; 2- adds it to chat history; 3- search data for answer; 
# 4- (optional) asks OpenAI; 5- adds response to chat history: 
if prompt := st.chat_input("Your question:"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    answer = get_answer_from_data(prompt, questions, answers)    
    if not answer:
        answer = get_answer_from_openai(prompt, st.session_state.chat_history, max_tokens, temperature)  
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "system":  # skips system messages
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
