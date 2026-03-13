from modules.module1_preprocessing import TamilPreprocessor
from modules.module2_entity_extraction import EntityExtractor
from modules.module3_knowledge_mapping import KnowledgeMapper
from modules.module4_sentence_generation import SentenceGenerator

import pickle


pre = TamilPreprocessor()
extractor = EntityExtractor()
mapper = KnowledgeMapper()
generator = SentenceGenerator()

validator = pickle.load(open("models/ettuthogai_validator.pkl","rb"))


def analyze_poem(poem):

    prediction = validator.predict([poem])[0]

    if prediction != "ETTUTHOGAI":

        return {
            "classification": prediction,
            "entities": [],
            "statistics": {},
            "metadata": {},
            "meaning": ""
        }

    tokens = pre.preprocess(poem)

    entities = extractor.predict(tokens)

    structured = mapper.enrich(entities)

    metadata = mapper.read_poem_metadata(poem)

    stats = mapper.entity_statistics(entities)

    meaning = generator.generate(entities)

    return {
        "entities": structured,
        "meaning": meaning,
        "statistics": stats,
        "metadata": metadata,
        "classification": prediction
    }