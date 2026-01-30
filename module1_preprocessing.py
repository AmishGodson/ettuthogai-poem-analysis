# # module1_preprocessing.py
# import re
# import unicodedata

# class TamilPreprocessor:
#     def __init__(self):
#         self.tamil_range = r"[^\u0B80-\u0BFF\s]"

#     def normalize(self, text):
#         return unicodedata.normalize("NFKC", text)

#     def remove_noise(self, text):
#         return re.sub(self.tamil_range, "", text)

#     def tokenize(self, text):
#         return text.split()

#     def preprocess(self, poem):
#         poem = self.normalize(poem)
#         poem = self.remove_noise(poem)
#         tokens = self.tokenize(poem)
#         return [t for t in tokens if t.strip()]

# # Test
# if __name__ == "__main__":
#     p = TamilPreprocessor()
#     print(p.preprocess("வேல் ஏந்தி போருக்கு சென்றான்"))
import re

class TamilPreprocessor:
    def preprocess(self, text):
        # Remove extra spaces from PDF copy
        text = re.sub(r"\s+", " ", text)
        return self.tokenize(text)

    def tokenize(self, text):
        return text.strip().split(" ")
