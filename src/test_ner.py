from src.ner import NamedEntityRecognizer

# Create an instance of the NER system
ner = NamedEntityRecognizer()

# Sample text for Named Entity Recognition
text = "Apple is looking to buy a startup in the UK for $1 billion by 2025."

# Extract entities from the text
entities = ner.extract_entities(text)

# Print the extracted entities
print("Entities:", entities)
