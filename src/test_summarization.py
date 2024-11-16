from src.summarization import Summarizer

# Create an instance of the Summarizer
summarizer = Summarizer()

# Sample text for summarization
text = """
Email summarization refers to the process of generating a concise version of a long email. Summarization 
involves the extraction of the most important information, reducing the overall length while maintaining 
the key points and message of the original content. This helps the recipient quickly understand the context 
without reading the entire email.
"""

# Summarize the email content
summary = summarizer.summarize_text(text)
print("Summary:", summary)
