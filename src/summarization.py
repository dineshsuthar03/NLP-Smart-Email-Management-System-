# Summarization Module 

# src/summarization.py
from transformers import pipeline

class Summarizer:
    def __init__(self):
        # Load pre-trained summarization model (T5/BART)
        self.summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

    def summarize_text(self, text: str):
        # Summarizing the text
        summary = self.summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']

# Example usage:
# summarizer = Summarizer()
# summary = summarizer.summarize_text("Your long email text goes here.")
# print(summary)
