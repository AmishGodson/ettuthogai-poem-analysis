import pickle
import os

MODEL_PATH = os.path.join("models", "ettuthogai_validator.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def validate_poem(poem_text, threshold=0.55):
    probs = model.predict_proba([poem_text])[0]
    classes = model.classes_

    ettu_index = list(classes).index("ETTUTHOGAI")
    confidence = probs[ettu_index]

    print(f"[DEBUG] Ettuthogai confidence: {confidence:.2f}")

    if confidence >= threshold:
        return "ETTUTHOGAI"
    return "NOT_ETTUTHOGAI"
