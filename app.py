import streamlit as st
from transformers import pipeline

# Load the Hugging Face model for health-related questions
model = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def get_response(user_input):
    response = model(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    return response

st.title("Health Symptoms Chatbot")

user_input = st.text_input("آپ کی علامات کے بارے میں بتائیں:")
if st.button("جواب حاصل کریں"):
    if user_input:
        response = get_response(user_input)
        st.text_area("چیٹ بوٹ:", value=response, height=300)
    else:
        st.warning("براہ کرم کوئی علامات درج کریں!")
