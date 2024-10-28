import streamlit as st

# Symptoms to disease mapping
symptom_disease_map = {
    "بخار": "انفیکشن، فلو، یا دیگر وائرل بیماری",
    "کھانسی": "نزلہ، برونکائٹس، یا نمونیا",
    "سردرد": "مائیگرین، تناؤ، یا خون کی کمی",
    "پیٹ میں درد": "معدے کا عارضہ، گیسٹروئنٹرائٹس",
    # مزید علامات اور بیماریوں کو شامل کریں
}

st.title("Health Symptoms Chatbot")

user_input = st.text_input("آپ کی علامات کے بارے میں بتائیں:")
if st.button("جواب حاصل کریں"):
    if user_input:
        # Check if the user input is in the mapping
        response = symptom_disease_map.get(user_input, "مجھے اس علامت کے بارے میں معلومات نہیں ہیں۔")
        st.text_area("چیٹ بوٹ:", value=response, height=300)
    else:
        st.warning("براہ کرم کوئی علامات درج کریں!")


