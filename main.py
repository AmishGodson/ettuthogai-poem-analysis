from main_logic import analyze_poem

if __name__ == "__main__":

    poem = input("Enter Tamil poem:\n")

    result = analyze_poem(poem)

    print("\nPoem Type:", result["classification"])

    if result["classification"] == "ETTUTHOGAI":

        print("\nPoem Details")
        print("Poem Number:", result["metadata"]["poem_number"])
        print("Book:", result["metadata"]["book"])
        print("Poet Tamil:", result["metadata"]["poet_tamil"])
        print("Poet English:", result["metadata"]["poet_english"])
        print("Category:", result["metadata"]["category"])
        print("Tinai:", result["metadata"]["tinai"])

        print("\nEntities\n")

        for e in result["entities"]:
            print(e["word"], "->", e["entity"], "|", e["explanation"])