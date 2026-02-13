from ettuthogai_validator import validate_poem
from ettuthogai_corpus_check import corpus_match

from module1_preprocessing import TamilPreprocessor
from module2_entity_extraction import EntityExtractor
from module3_knowledge_mapping import KnowledgeMapper
from module4_sentence_generation import TamilSentenceGenerator


def analyze_poem(poem_text):
    result = validate_poem(poem_text)

    if result == "ETTUTHOGAI":
        validation = "Ettuthogai poem detected (ML)"
    elif corpus_match(poem_text):
        validation = "Ettuthogai poem detected (Corpus fallback)"
    else:
        return {
            "validation": "Not an Ettuthogai poem",
            "tokens": [],
            "entities": [],
            "meaning": ""
        }

    pre = TamilPreprocessor()
    tokens = pre.preprocess(poem_text)

    ner = EntityExtractor()
    entities = ner.predict(tokens)

    kb = KnowledgeMapper()
    enriched = kb.enrich(entities)

    gen = TamilSentenceGenerator()
    meaning = gen.generate(enriched)

    return {
        "validation": validation,
        "tokens": tokens,
        "entities": entities,
        "meaning": meaning
    }
