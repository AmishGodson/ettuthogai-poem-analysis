# train_model.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense
import numpy as np

VOCAB_SIZE = 5000
TAG_SIZE = 8   # O, KING, PLACE, WEAPON, EVENT, EMOTION, CULTURE, DYNASTY

model = Sequential([
    Embedding(VOCAB_SIZE, 128, mask_zero=True),
    Bidirectional(LSTM(128, return_sequences=True)),
    Dense(TAG_SIZE, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Dummy training data for structure
X = np.random.randint(1, VOCAB_SIZE, (100, 20))
y = np.random.randint(0, TAG_SIZE, (100, 20))

model.fit(X, y, epochs=5, batch_size=16)
model.save("models/bilstm_ner.h5")
