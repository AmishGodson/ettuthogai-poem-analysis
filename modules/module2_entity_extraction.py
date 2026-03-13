import csv
import os

class EntityExtractor:

    _entity_dict = None

    def __init__(self):

        if EntityExtractor._entity_dict is None:

            EntityExtractor._entity_dict = {}

            folders = [
                "data/ettuthogai/csv",
                "data/ettuthogai/csv_2"
            ]

            for folder in folders:

                if not os.path.exists(folder):
                    continue

                for file in os.listdir(folder):

                    if not file.endswith(".csv"):
                        continue

                    path = os.path.join(folder, file)

                    with open(path, encoding="utf-8-sig") as f:

                        reader = csv.DictReader(f)

                        for row in reader:

                            word = (row.get("Word") or "").strip()
                            tag = (row.get("Entity") or "O").strip()
                            explanation = (row.get("Explanation") or "").strip()

                            if not explanation:
                                explanation = "-"

                            if word:

                                EntityExtractor._entity_dict[word] = {
                                    "entity": tag,
                                    "explanation": explanation
                                }

            print("Entities loaded:", len(EntityExtractor._entity_dict))

        self.entity_dict = EntityExtractor._entity_dict


    def predict(self, tokens):

        result = []

        for token_data in tokens:

            token = token_data["word"]

            data = self.entity_dict.get(token)

            if data:

                tag = data["entity"]
                exp = data["explanation"]

            else:

                tag = "O"
                exp = "-"

            result.append({
                "word": token,
                "entity": tag,
                "explanation": exp
            })

        return result