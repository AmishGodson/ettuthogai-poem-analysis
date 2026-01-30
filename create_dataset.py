import csv
import os

ETTUTHOGAI_FILE = "data/ettuthogai/agananuru.txt"
NON_ETTUTHOGAI_FILE = "data/non_ettuthogai/other_tamil.txt"
OUTPUT_FILE = "data/ettuthogai_classifier.csv"

def read_poems(path):
    poems = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # keep only meaningful lines
            if len(line) >= 15:
                poems.append(line)
    return poems

ettuthogai_poems = read_poems(ETTUTHOGAI_FILE)
non_ettuthogai_poems = read_poems(NON_ETTUTHOGAI_FILE)

# Safety check (important for review)
if len(ettuthogai_poems) < 5:
    print("⚠️ Warning: Very small Ettuthogai dataset")

os.makedirs("data", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])

    for poem in ettuthogai_poems:
        writer.writerow([poem, "ETTUTHOGAI"])

    for poem in non_ettuthogai_poems:
        writer.writerow([poem, "NOT_ETTUTHOGAI"])

print("✅ Dataset created successfully")
print("ETTUTHOGAI samples:", len(ettuthogai_poems))
print("NON-ETTUTHOGAI samples:", len(non_ettuthogai_poems))
