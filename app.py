import streamlit as st

# Symptoms to disease mapping with advice
symptom_disease_map = {
    "بخار": {
        "disease": "فلو",
        "advice": "زیادہ پانی پئیں، آرام کریں، اور ڈاکٹر سے مشورہ کریں۔"
    },
    "کھانسی": {
        "disease": "نزلہ",
        "advice": "گرم مشروبات لیں اور اگر علامات برقرار رہیں تو ڈاکٹر سے رجوع کریں۔"
    },
    "سردرد": {
        "disease": "مائیگرین",
        "advice": "آرام کریں، اور اگر درد بڑھتا ہے تو ڈاکٹر سے مشورہ کریں۔"
    },
    "پیٹ میں درد": {
        "disease": "معدے کا عارضہ",
        "advice": "ہلکا پھلکا کھانا کھائیں اور پانی پیئیں، اگر درد برقرار رہے تو ڈاکٹر سے ملیں۔"
    },
    # مزید علامات اور ان کے مشورے شامل کریں
}

st.title("Health Symptoms Chatbot")

user_input = st.text_input("آپ کی علامات کے بارے میں بتائیں:")
if st.button("جواب حاصل کریں"):
    if user_input:
        # Check if the user input is in the mapping
        response = symptom_disease_map.get(user_input)
        if response:
            st.text_area("بیماری:", value=response['disease'], height=100)
            st.text_area("مشورہ:", value=response['advice'], height=300)
        else:
            st.text_area("چیٹ بوٹ:", value="مجھے اس علامت کے بارے میں معلومات نہیں ہیں۔", height=300)
    else:
        st.warning("براہ کرم کوئی علامات درج کریں!")



