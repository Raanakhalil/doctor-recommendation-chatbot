import streamlit as st

# Symptoms to disease mapping with advice
symptom_disease_map = {
    "fever": {
        "disease": "Flu",
        "advice": "Drink plenty of water, rest, and consult a doctor."
    },
    "cough": {
        "disease": "Cold",
        "advice": "Drink warm beverages and see a doctor if symptoms persist."
    },
    "headache": {
        "disease": "Migraine",
        "advice": "Rest and consult a doctor if the pain worsens."
    },
    "stomach pain": {
        "disease": "Gastrointestinal issue",
        "advice": "Eat light meals and stay hydrated; consult a doctor if pain persists."
    },
    # Add more symptoms and their corresponding advice
}

st.title("Health Symptoms Chatbot")

user_input = st.text_input("Describe your symptoms:")
if st.button("Get Response"):
    if user_input:
        # Check if the user input is in the mapping
        response = symptom_disease_map.get(user_input.lower())
        if response:
            st.text_area("Disease:", value=response['disease'], height=100)
            st.text_area("Advice:", value=response['advice'], height=300)
        else:
            st.text_area("Chatbot:", value="I don't have information about this symptom.", height=300)
    else:
        st.warning("Please enter some symptoms!")




