class EntityExtractor:
    def __init__(self, model_path=None):
        self.model_path = model_path  # BiLSTM (optional for demo)

    def predict(self, tokens):
        entity_rules = {
            # DEITIES
            "சிவன்": "DEITY",
            "முருகன்": "DEITY",
            "பெருமான்": "DEITY",
            "பிறை": "SYMBOL",

            # WAR / POWER
            "வேல்": "WEAPON",
            "மழு": "WEAPON",
            "போர்": "EVENT",

            # NATURE (important for your poems)
            "கார்": "NATURE",
            "மலர்": "NATURE",
            "முல்லை": "TINAI",
            "காடு": "NATURE",
            "மழை": "NATURE",
            "வானம்": "NATURE",
            "மலை": "NATURE",

            # ANIMALS
            "யானை": "ANIMAL",
            "முதலை": "ANIMAL",
            "புலி": "ANIMAL",
            "குரங்கு": "ANIMAL",
            "பறவை": "ANIMAL",

            # EMOTIONS / ABSTRACT
            "அஞ்ச": "EMOTION",
            "துயர்": "EMOTION",
            "காத்திருப்பு": "EMOTION",
            "பொய்": "SPEECH"
        }

        tagged = []
        for token in tokens:
            tag = "O"
            for key in entity_rules:
                if key in token:
                    tag = entity_rules[key]
            tagged.append((token, tag))

        return tagged
