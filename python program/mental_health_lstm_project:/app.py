import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model & tokenizer
model = load_model("lstm_model.h5")
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

labels_map = {
    0: "Depressed",
    1: "Stressed",
    2: "Normal"
}

def predict_mental_state(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=100)
    prediction = np.argmax(model.predict(padded), axis=1)[0]
    return labels_map[prediction]

# ===== UI =====
st.set_page_config(page_title="Mental Health LSTM Analyzer")

st.title("🧠 Mental Health Analysis (LSTM)")
st.write("Deep Learning based mental health prediction")

user_text = st.text_area("✍ Enter your thoughts:")

if st.button("Analyze"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        result = predict_mental_state(user_text)

        if result == "Depressed":
            st.error("⚠ Mental State: Depressed")
        elif result == "Stressed":
            st.warning("⚠ Mental State: Stressed")
        else:
            st.success("✅ Mental State: Normal")
