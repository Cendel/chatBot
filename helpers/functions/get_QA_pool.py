import streamlit as st
import pandas as pd

def get_QA_pool():
    try:
        data = pd.read_excel("././Mentoring_data.xlsx")
        questions = data["Question"].tolist() if "Question" in data.columns else []
        answers = data["Answer"].tolist() if "Answer" in data.columns else []
        
        if not questions or not answers:
            st.error("There are no Question or Answer columns in the file.")
    except Exception as e:
        st.error(f"Error loading data file: {str(e)}")
    
    return questions, answers