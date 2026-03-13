import re

# punctuation removal for tokenization
pattern = re.compile(r"[,:;.!?()\[\]{}\-—–]")

# Tamil + punctuation validation
tamil_allowed = re.compile(r'^[\u0B80-\u0BFF\s,.;:!?()\[\]\-—–]+$')


class TamilPreprocessor:

    def preprocess(self, text):

        text = text.strip()

        # Validate Tamil + punctuation only
        if not tamil_allowed.match(text):

            raise ValueError("Only Tamil words and punctuation are allowed")

        # remove punctuation for tokenization
        text = pattern.sub(" ", text)

        tokens = text.split()

        result = []

        for token in tokens:

            result.append({
                "word": token
            })

        return result