# Named Entity Recognition Module 
# src/named_entity_recognition.py
# import spacy

# class NER:
#     def __init__(self):
#         # Load the pre-trained SpaCy NER model
#         self.nlp = spacy.load("en_core_web_sm")

#     def extract_entities(self, text: str):
#         # Process the text through SpaCy's pipeline
#         doc = self.nlp(text)
#         entities = [(ent.text, ent.label_) for ent in doc.ents]
#         return entities

# Example usage:
# ner = NER()
# entities = ner.extract_entities("Apple is looking to buy a startup in San Francisco.")
# print(entities)




# src/ner.py
import spacy

class NamedEntityRecognizer:
    def __init__(self):
        # Load the pre-trained spaCy model for NER (en_core_web_sm)
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text: str):
        # Process the text with spaCy
        doc = self.nlp(text)

        # Extract entities
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities

# # Example usage:
# ner = NamedEntityRecognizer()
# entities = ner.extract_entities("Apple is looking to buy a startup in the UK for $1 billion by 2025.")
# print(entities)
