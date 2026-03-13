import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

DATA_FILE = "data/ettuthogai_dataset.csv"

data = pd.read_csv(DATA_FILE)

X = data["text"]
y = data["label"]

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        analyzer="char",
        ngram_range=(3,5)
    )),
    ("clf", LinearSVC())
])

model.fit(X,y)

with open("models/ettuthogai_validator.pkl","wb") as f:
    pickle.dump(model,f)

print("Validator model trained")