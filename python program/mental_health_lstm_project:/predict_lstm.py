import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("lstm_model.h5")
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

labels = {0: "Depressed", 1: "Stressed", 2: "Normal"}

def predict_mental_state(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=100)
    prediction = np.argmax(model.predict(padded), axis=1)[0]
    return labels[prediction]

if __name__ == "__main__":
    text = "I feel lonely and exhausted"
    print("Prediction:", predict_mental_state(text))
