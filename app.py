import streamlit as st
from transformers import pipeline

# Load the Hugging Face model for health-related questions
@st.cache_resource  # Caching the model for efficiency
def load_model():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

model = load_model()

st.title("Health Symptoms Chatbot")

user_input = st.text_input("آپ کی علامات کے بارے میں بتائیں:")
if st.button("جواب حاصل کریں"):
    if user_input:
        # Example of a context that can be improved based on your needs
        context = "اگر آپ کو بخار، کھانسی، یا سانس لینے میں مشکل ہو رہی ہے، تو یہ علامات عام طور پر انفیکشن کی نشانی ہو سکتی ہیں۔"
        response = model(question=user_input, context=context)
        st.text_area("چیٹ بوٹ:", value=response['answer'], height=300)
    else:
        st.warning("براہ کرم کوئی علامات درج کریں!")

