import os
import re


class KnowledgeMapper:

    def enrich(self, entities):

        structured = []

        for e in entities:

            structured.append({
                "word": e["word"],
                "entity": e["entity"],
                "explanation": e["explanation"]
            })

        return structured


    def entity_statistics(self, entities):

        stats = {}

        for e in entities:

            tag = e["entity"]

            stats[tag] = stats.get(tag, 0) + 1

        return stats


    def read_poem_metadata(self, poem_text):

        folder = "data/ettuthogai/text_2"

        user_lines = poem_text.strip().split("\n")

        user_lines = [l.strip(" ,.") for l in user_lines if l.strip()]

        for file in os.listdir(folder):

            if not file.endswith(".txt"):
                continue

            path = os.path.join(folder, file)

            with open(path, encoding="utf-8") as f:

                content = f.read()

                poems = content.split("---")

                for poem in poems:

                    poem_number=""
                    poet_tamil=""
                    poet_english=""
                    category=""
                    tinai=""

                    lines=[]
                    reading=False

                    for line in poem.split("\n"):

                        line=line.strip()

                        if line.startswith("POEM_NUMBER"):
                            poem_number=line.split(":")[1].strip()

                        elif line.startswith("AUTHOR_TAMIL"):
                            poet_tamil=line.split(":")[1].strip()

                        elif line.startswith("AUTHOR_ENGLISH"):
                            poet_english=line.split(":")[1].strip()

                        elif line.startswith("CATEGORY"):
                            category=line.split(":")[1].strip()

                        elif line.startswith("TINAI"):
                            tinai=line.split(":")[1].strip()

                        elif line.startswith("LINES"):
                            reading=True

                        elif reading and line:

                            m=re.match(r"\d+\.\s*(.*)",line)

                            if m:
                                lines.append(m.group(1).strip(" ,."))

                    match_count=0

                    for ul in user_lines:

                        for pl in lines:

                            if ul in pl:
                                match_count+=1

                    if match_count>=1:

                        return {
                            "poem_number":poem_number,
                            "book":file.replace(".txt",""),
                            "poet_tamil":poet_tamil,
                            "poet_english":poet_english,
                            "category":category,
                            "tinai":tinai
                        }

        return {
            "poem_number":"",
            "book":"",
            "poet_tamil":"",
            "poet_english":"",
            "category":"",
            "tinai":""
        }