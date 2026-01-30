class KnowledgeMapper:
    def __init__(self, kb_path=None):
        self.kb_path = kb_path

    def enrich(self, entities):
        enriched = []
        for token, tag in entities:
            enriched.append({
                "token": token,
                "entity": tag
            })
        return enriched
