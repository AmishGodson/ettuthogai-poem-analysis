import csv
import os

class EntityExtractor:
    def __init__(self, csv_file="data/paripadal_entities.csv"):
        self.entity_dict = {}

        if os.path.exists(csv_file):
            with open(csv_file, encoding="utf-8") as f:
                reader = csv.DictReader(f)

                print("CSV Columns Found:", reader.fieldnames)

                for row in reader:
                    # Use your exact column names
                    token = row.get("Word_Original")
                    label = row.get("Hierarchical_Entity_Tag")

                    if token and label:
                        self.entity_dict[token.strip()] = label.strip()

    def predict(self, tokens):
        tagged = []

        for token in tokens:
            tag = "O"

            # Exact match
            if token in self.entity_dict:
                tag = self.entity_dict[token]

            # Substring match (for Tamil suffix words)
            else:
                for key, val in self.entity_dict.items():
                    if key in token:
                        tag = val
                        break

            tagged.append((token, tag))

        return tagged
