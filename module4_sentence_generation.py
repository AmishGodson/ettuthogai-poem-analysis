class TamilSentenceGenerator:
    def generate(self, enriched_entities):
        entities = {e["entity"] for e in enriched_entities}

        if "DEITY" in entities:
            return (
                "இந்த பாடல் தெய்வத்தின் தொன்மையான உருவத்தையும் "
                "அதன் ஆன்மிக மகத்துவத்தையும் விளக்குகிறது."
            )

        if "WEAPON" in entities or "EVENT" in entities:
            return (
                "இந்த பாடலில் போர்ச்சூழலும் வீரத்தின் வெளிப்பாடும் "
                "சித்தரிக்கப்படுகின்றன."
            )

        if "TINAI" in entities or "NATURE" in entities:
            return (
                "இந்த பாடலில் இயற்கை அழகும் சங்ககால அகத்திணை "
                "உணர்வுகளும் வெளிப்படுகின்றன."
            )

        if "EMOTION" in entities:
            return (
                "இந்த பாடல் காதல், துயரம் அல்லது மனக்குழப்பம் போன்ற "
                "உள்ளுணர்வுகளை வெளிப்படுத்துகிறது."
            )

        return "இந்த பாடல் சங்ககால வாழ்க்கை முறையை விளக்குகிறது."
