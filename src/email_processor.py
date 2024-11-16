# Email Processor Module 
# src/email_processor.py
from summarization import Summarizer
from spam_detection import SpamDetector
from ner import NER

class EmailProcessor:
    def __init__(self):
        self.summarizer = Summarizer()
        self.spam_detector = SpamDetector()
        self.ner = NER()

    def process_email(self, email_text: str):
        # Summarize the email
        summary = self.summarizer.summarize_text(email_text)
        
        # Check if the email is spam
        spam_status = self.spam_detector.predict(email_text)

        # Extract named entities
        entities = self.ner.extract_entities(email_text)

        return {
            'summary': summary,
            'spam_status': spam_status,
            'entities': entities
        }

# Example usage:
# email_processor = EmailProcessor()
# result = email_processor.process_email("Your email content here.")
# print(result)
