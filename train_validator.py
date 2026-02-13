import os
import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

DATA_FILE = "data/ettuthogai_dataset.csv"

# Create models folder
os.makedirs("models", exist_ok=True)

# Load dataset
data = pd.read_csv(DATA_FILE)

X = data["text"]
y = data["label"]

# Pipeline model
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 4)
    )),
    ("clf", MultinomialNB())
])

# Train
model.fit(X, y)

# Save model
with open("models/ettuthogai_validator.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully")
print("Saved as models/ettuthogai_validator.pkl")
