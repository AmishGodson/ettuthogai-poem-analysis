class SentenceGenerator:

    def generate(self, entities):

        counts = {}

        for e in entities:

            tag = e["entity"]

            if tag == "O":
                continue

            counts[tag] = counts.get(tag, 0) + 1


        # If ALL entities are O
        if not counts:

            return (
                "இது ஒரு சங்ககால பாடல் ஆகும்.\n"
                "This is a Sangam period poem describing classical Tamil cultural poetic tradition."
            )


        max_count = max(counts.values())

        dominant = [k for k,v in counts.items() if v == max_count]

        meanings = []


        for tag in dominant:


            if tag == "PERSON":

                meanings.append(
                "இந்த பாடல் மனிதர்கள் உறவு உணர்வுகள் காதல் பிரிவு நினைவுகளை கவிதை காட்சிகளால் வெளிப்படுத்துகிறது.\n"
                "Human relationships emotions love separation memories experiences dominate thematic imagery within poem."
                )


            elif tag == "KING":

                meanings.append(
                "இந்த பாடல் அரசர்கள் ஆட்சி வீரியம் புகழ் அரசியல் அதிகாரம் காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Royal authority kingship valor leadership political power dominate thematic imagery of poem."
                )


            elif tag == "POET":

                meanings.append(
                "இந்த பாடல் கவிஞரின் கற்பனை உணர்வு இலக்கிய பார்வையை வெளிப்படுத்துகிறது.\n"
                "Poetic imagination artistic expression literary voice emotional creativity dominate poem meaning."
                )


            elif tag == "PROFESSION":

                meanings.append(
                "இந்த பாடல் தொழில்கள் சமூக வாழ்க்கை நாளாந்த செயல்களை விவரிக்கிறது.\n"
                "Occupational roles livelihood social activity daily life themes dominate poem imagery."
                )


            elif tag == "WARRIOR":

                meanings.append(
                "இந்த பாடல் போராட்டம் வீரர்கள் தைரியம் பாதுகாப்பு காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Warriors courage battlefield defense warfare imagery dominates meaning of poem."
                )


            elif tag == "TRIBE":

                meanings.append(
                "இந்த பாடல் பழங்குடி சமூக மரபுகள் வாழ்க்கை முறைகளை விவரிக்கிறது.\n"
                "Tribal communities traditions cultural identity lifestyle imagery appear within poem."
                )


            elif tag == "PLACE":

                meanings.append(
                "இந்த பாடல் குறிப்பிட்ட ஊர் இடம் வாழ்க்கை சூழலை விவரிக்கிறது.\n"
                "Specific places settlements landscape environment imagery dominate poem meaning."
                )


            elif tag == "REGION":

                meanings.append(
                "இந்த பாடல் பரந்த நிலப்பகுதி மக்களின் வாழ்க்கை சூழலை வெளிப்படுத்துகிறது.\n"
                "Geographical regions territory landscape environment imagery dominate poem interpretation."
                )


            elif tag == "MOUNTAIN":

                meanings.append(
                "இந்த பாடல் மலைப்பகுதி குறிஞ்சி நிலம் காதல் காத்திருப்பு காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Mountain Kurinji landscape love waiting natural scenery imagery dominates poem."
                )


            elif tag == "FOREST":

                meanings.append(
                "இந்த பாடல் காடு முல்லை நிலம் அமைதி இயற்கை காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Forest Mullai landscape calm nature environment imagery dominates poem meaning."
                )


            elif tag == "FIELD":

                meanings.append(
                "இந்த பாடல் விவசாய நிலம் மருத நிலம் கிராம வாழ்க்கையை விவரிக்கிறது.\n"
                "Agricultural Marutham landscape farming prosperity rural life imagery dominates poem."
                )


            elif tag == "WATERBODY":

                meanings.append(
                "இந்த பாடல் கடல் நதி நீர்நிலைகள் வாழ்க்கை பயணம் காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Sea rivers water bodies livelihood travel environment imagery dominate poem."
                )


            elif tag == "DESERT":

                meanings.append(
                "இந்த பாடல் பாலை நிலம் வறண்ட பயணம் பிரிவு காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Desert Palai landscape separation hardship journey imagery dominates poem meaning."
                )


            elif tag == "ANIMAL":

                meanings.append(
                "இந்த பாடலில் விலங்குகள் இயற்கை வாழ்க்கை காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Animals symbolize natural environment instincts life interaction imagery dominates poem."
                )


            elif tag == "BIRD":

                meanings.append(
                "இந்த பாடலில் பறவைகள் இயற்கை இயக்க அழகை வெளிப்படுத்துகின்றன.\n"
                "Bird imagery freedom movement nature beauty symbolism dominates poem scenes."
                )


            elif tag == "INSECT":

                meanings.append(
                "இந்த பாடலில் பூச்சிகள் இயற்கை சூழல் உயிரியல் காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Insects symbolize ecological life natural interaction imagery within poem."
                )


            elif tag == "FISH":

                meanings.append(
                "இந்த பாடலில் மீன்கள் நீர்நிலை வாழ்க்கை காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Fish imagery water ecosystem livelihood natural symbolism appears prominently."
                )


            elif tag == "PLANT":

                meanings.append(
                "இந்த பாடலில் செடிகள் மரங்கள் இயற்கை சூழலை வெளிப்படுத்துகின்றன.\n"
                "Plants trees vegetation landscape ecological imagery dominates poem meaning."
                )


            elif tag == "FLOWER":

                meanings.append(
                "இந்த பாடலில் மலர்கள் அழகு காதல் உணர்வு காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Flowers symbolize beauty love emotions nature imagery across poem."
                )


            elif tag == "FRUIT":

                meanings.append(
                "இந்த பாடலில் பழங்கள் வளம் இயற்கை உணவு காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Fruit imagery abundance nourishment natural life symbolism dominates poem."
                )


            elif tag == "FOOD":

                meanings.append(
                "இந்த பாடலில் உணவு வாழ்க்கை வளம் சமூகம் காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Food imagery livelihood prosperity culture daily life themes dominate poem."
                )


            elif tag == "WEAPON":

                meanings.append(
                "இந்த பாடலில் ஆயுதங்கள் போராட்ட வீரத்தை வெளிப்படுத்துகின்றன.\n"
                "Weapons symbolize warfare defense courage themes dominating imagery."
                )


            elif tag == "VEHICLE":

                meanings.append(
                "இந்த பாடலில் வாகனங்கள் பயணம் இயக்கத்தை வெளிப்படுத்துகின்றன.\n"
                "Vehicles symbolize travel movement journeys transitions imagery in poem."
                )


            elif tag == "OBJECT":

                meanings.append(
                "இந்த பாடலில் பொருட்கள் கருவிகள் வாழ்க்கை பயன்பாட்டை வெளிப்படுத்துகின்றன.\n"
                "Objects artifacts symbolize culture tools practical life imagery."
                )


            elif tag == "CLOTHING":

                meanings.append(
                "இந்த பாடலில் உடைகள் ஆபரணங்கள் சமூக அடையாளத்தை வெளிப்படுத்துகின்றன.\n"
                "Clothing ornaments symbolize status identity culture imagery."
                )


            elif tag == "STRUCTURE":

                meanings.append(
                "இந்த பாடலில் கட்டிடங்கள் நகர அமைப்பு காட்சிகளை வெளிப்படுத்துகின்றன.\n"
                "Buildings structures settlements architecture imagery dominate poem themes."
                )


            elif tag == "DEITY":

                meanings.append(
                "இந்த பாடல் தெய்வங்கள் ஆன்மீகம் பக்தி நம்பிக்கைகளை வெளிப்படுத்துகிறது.\n"
                "Deities symbolize spirituality devotion divine presence imagery."
                )


            elif tag == "MYTH":

                meanings.append(
                "இந்த பாடலில் புராண உருவங்கள் கற்பனை உலகத்தை வெளிப்படுத்துகின்றன.\n"
                "Mythical beings fantasy imagination symbolism appear within poem."
                )


            elif tag == "NATURE":

                meanings.append(
                "இந்த பாடல் இயற்கை சூழல் காலநிலை காட்சிகளை வெளிப்படுத்துகிறது.\n"
                "Nature environment climate scenery imagery dominates poem themes."
                )


        return "\n\n".join(meanings)