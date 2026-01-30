import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from ettuthogai_validator import validate_poem
from ettuthogai_corpus_check import corpus_match

from module1_preprocessing import TamilPreprocessor
from module2_entity_extraction import EntityExtractor
from module3_knowledge_mapping import KnowledgeMapper
from module4_sentence_generation import TamilSentenceGenerator

# ---- READ INPUT ----
with open("input_poem.txt", encoding="utf-8") as f:
    poem = f.read().strip()

print("Poem read from file:", poem)

# ---- VALIDATION ----
ml_result = validate_poem(poem)

if ml_result == "ETTUTHOGAI":
    print("✅ Ettuthogai poem detected (ML)")
elif corpus_match(poem):
    print("✅ Ettuthogai poem detected (Corpus-based fallback)")
else:
    print("❌ This poem is NOT an Ettuthogai poem.")
    exit()

# ---- SEMANTIC PIPELINE ----
pre = TamilPreprocessor()
tokens = pre.preprocess(poem)

ner = EntityExtractor()
entities = ner.predict(tokens)

kb = KnowledgeMapper()
enriched = kb.enrich(entities)

gen = TamilSentenceGenerator()
meaning = gen.generate(enriched)

# ---- OUTPUT ----
print("TOKENS:", tokens)
print("ENTITY TAGS:", entities)
print("SIMPLIFIED MEANING:", meaning)
