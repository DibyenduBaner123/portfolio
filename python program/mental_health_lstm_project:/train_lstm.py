# ===== macOS TensorFlow FIX (MUST BE FIRST) =====
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# ===== Imports =====
import pandas as pd
import numpy as np
import pickle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# ===== Load dataset =====
df = pd.read_csv("data/mental_health_text.csv")

texts = df["text"].values
labels = df["label"].values

# ===== Tokenization =====
tokenizer = Tokenizer(num_words=3000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=100)

# ===== Train-test split =====
X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, labels, test_size=0.2, random_state=42
)

# ===== Build LSTM model =====
model = Sequential([
    Embedding(input_dim=3000, output_dim=32),
    LSTM(32),
    Dense(3, activation="softmax")
])

# ✅ THIS WAS MISSING BEFORE (NOW FIXED)
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ===== Train model =====
model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=4,
    validation_data=(X_test, y_test)
)

# ===== Save model & tokenizer =====
model.save("lstm_model.h5")
pickle.dump(tokenizer, open("tokenizer.pkl", "wb"))

print("✅ LSTM model and tokenizer saved successfully!")
