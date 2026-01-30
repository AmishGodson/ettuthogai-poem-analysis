import os
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

os.makedirs("models", exist_ok=True)

data = pd.read_csv("data/ettuthogai_classifier.csv")

X = data["text"]
y = data["label"]

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 4)   # good for Tamil morphology
    )),
    ("clf", MultinomialNB())
])

model.fit(X, y)

with open("models/ettuthogai_validator.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Ettuthogai validator trained")
