import csv

input_file = "aingurunooru.csv"
output_file = "fixed.csv"

EXPECTED_COLUMNS = 12

fixed_rows = []

with open(input_file, encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:

        if len(row) == EXPECTED_COLUMNS:
            fixed_rows.append(row)
        else:
            # merge extra columns back into the meaning_of_line field
            while len(row) > EXPECTED_COLUMNS:
                row[6] = row[6] + "," + row[7]
                del row[7]

            fixed_rows.append(row)

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(fixed_rows)

print("CSV repaired successfully!")