import pickle
import os

MODEL_PATH = os.path.join("models", "ettuthogai_validator.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def validate_poem(poem_text):
    """
    Returns:
    - ETTUTHOGAI
    - NOT_ETTUTHOGAI
    """

    prediction = model.predict([poem_text])[0]

    # Decision score (confidence-like)
    score = model.decision_function([poem_text])[0]

    print(f"[DEBUG] Decision score: {score:.2f}")

    return prediction
