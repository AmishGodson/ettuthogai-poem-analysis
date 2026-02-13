import os
import csv

ETTUTHOGAI_FOLDER = "data/ettuthogai"
NON_FOLDER = "data/non_ettuthogai"

OUTPUT_FILE = "data/ettuthogai_dataset.csv"


def read_poems(folder):
    poems = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if len(line) > 20:
                        poems.append(line)
    return poems


ettuthogai_poems = read_poems(ETTUTHOGAI_FOLDER)
non_poems = read_poems(NON_FOLDER)

with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])

    for p in ettuthogai_poems:
        writer.writerow([p, "ETTUTHOGAI"])

    for p in non_poems:
        writer.writerow([p, "NOT_ETTUTHOGAI"])

print("Dataset created successfully")
print("Ettuthogai samples:", len(ettuthogai_poems))
print("Non-Ettuthogai samples:", len(non_poems))
