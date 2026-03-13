import pickle

with open("models/ettuthogai_validator.pkl","rb") as f:
    model = pickle.load(f)

poem = "கார்வானம் கொண்டனைப் பொன்னேர் புதுமலர்த் தாரன்"

result = model.predict([poem])[0]

print("Prediction:",result)