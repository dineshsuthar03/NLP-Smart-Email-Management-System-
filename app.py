from flask import Flask, request, jsonify, render_template
from src.summarization import Summarizer
from src.spam_detection import SpamDetector
from src.ner import NamedEntityRecognizer
import os
from flask_cors import CORS  # Import CORS

# Initialize the components
summarizer = Summarizer()
ner = NamedEntityRecognizer()
import joblib

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Load the model (including the fitted vectorizer)
spam_detector = SpamDetector()

@app.route('/')
def index():
    return render_template('index.html')

# Route for detecting spam
@app.route('/detect_spam', methods=['POST'])
def detect_spam():
    data = request.get_json()
    text = data.get('text', '')
    
    try:
        # Predict using SpamDetector
        result = spam_detector.predict(text)
        if isinstance(result, dict) and 'isSpam' in result:
            return jsonify({"isSpam": result['isSpam']}), 200
        else:
            raise ValueError("Unexpected result format from SpamDetector")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for text summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    
    # Handle empty or invalid text input
    if not text:
        return jsonify({"error": "No text provided for summarization"}), 400
    
    summary = summarizer.summarize_text(text)
    return jsonify({"summary": summary})

# Route for named entity recognition
@app.route('/ner', methods=['POST'])
def recognize_entities():
    data = request.get_json()
    text = data.get('text', '')
    
    # Handle empty or invalid text input
    if not text:
        return jsonify({"error": "No text provided for named entity recognition"}), 400
    
    entities = ner.extract_entities(text)
    return jsonify({"entities": entities})

if __name__ == '__main__':
    # Ensure the templates folder exists
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Run the app
    app.run(debug=True)
