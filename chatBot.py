import streamlit as st
import pandas as pd
import openai
from difflib import get_close_matches

openai.api_key = st.secrets["OPENAI_API_KEY"]  # Streamlit secrets kullanarak API anahtarını alıyoruz

# uploads question-answer pool:
try:
    data = pd.read_excel("Mentoring_data.xlsx")
    questions = data["Question"].tolist() if "Question" in data.columns else []
    answers = data["Answer"].tolist() if "Answer" in data.columns else []
    
    if not questions or not answers:
        st.error("Mentoring_data.xlsx dosyasındaki 'Question' veya 'Answer' sütunları eksik veya boş.")
except Exception as e:
    st.error(f"Error loading data file: {str(e)}")

# matching the closest answer to the question:
def get_answer_from_data(prompt):
    if questions:
        closest_match = get_close_matches(prompt, questions, n=1, cutoff=0.5)
        if closest_match:
            match_index = questions.index(closest_match[0])
            return answers[match_index]
    return None  

# retrieves answers from OpenAI API:
def get_response_from_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Always answer in the language in which the question is asked, and always end your answer with a related emoji: {prompt}"}
            ],
            max_tokens=150,
            temperature=1
        )
        generated_text = response['choices'][0]['message']['content'].strip()
        return generated_text
    except Exception as e:
        return f"Error: {str(e)}"

# heading:
st.header("Chat with Techpro Education 🤖")

# starts chat history:
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Data Science!"}
    ]

# Kullanıcı girişi ve yanıt oluşturma
if prompt := st.chat_input("Your question:"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Önce dosyadan yanıt bulmaya çalış
    answer = get_answer_from_data(prompt)
    if not answer:
        # Dosyada yanıt yoksa, OpenAI API'den yanıt al
        answer = get_response_from_openai(prompt)

    # Yanıtı ekrana yazdırma ve sohbet geçmişine ekleme
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Önceki sohbet mesajlarını gösterme
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
