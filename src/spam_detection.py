import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os


class SpamDetector:
    def __init__(self):
        """
        Initialize the spam detector with a TF-IDF vectorizer and a logistic regression model.
        """
        self.vectorizer_path = r'src\vectorizer.pkl'
        self.model_path = r'src\spam_model.pkl'
        
        # Initialize vectorizer and model
        self.vectorizer = None
        self.model = None
        
        # Load the model and vectorizer if they exist
        self._load_model()

    def _load_model(self):
        """
        Load the model and vectorizer from disk.
        """
        if os.path.exists(self.vectorizer_path) and os.path.exists(self.model_path):
            with open(self.vectorizer_path, 'rb') as vec_file:
                self.vectorizer = joblib.load(vec_file)
            with open(self.model_path, 'rb') as model_file:
                self.model = joblib.load(model_file)
            print("Model and vectorizer loaded successfully.")
        else:
            print("Model or vectorizer not found. Please train the model first.")
        
    def train(self, data_path):
        """
        Train the spam detection model using the dataset at the specified path.
        Args:
            data_path (str): Path to the CSV file containing the dataset.
        """
        # Load the dataset
        data = pd.read_csv(data_path)
        X = data['text']
        y = data['label']

        # Vectorize the text data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        X_vec = self.vectorizer.fit_transform(X)

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

        # Train the model
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        # Save the vectorizer and model
        with open(self.vectorizer_path, 'wb') as vec_file:
            joblib.dump(self.vectorizer, vec_file)
        with open(self.model_path, 'wb') as model_file:
            joblib.dump(self.model, model_file)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print(f"Training complete. Accuracy: {accuracy_score(y_test, y_pred)}")

    def predict(self, text):
        """
        Predict if the given text is spam or not.
        Args:
            text (str): The input text to classify.
        Returns:
            dict: A dictionary containing the prediction result.
        """
        # Ensure model and vectorizer are loaded
        if not self.vectorizer or not self.model:
            self._load_model()
            if not self.vectorizer or not self.model:
                raise FileNotFoundError("Model or vectorizer file not found. Please train the model first.")

        # Transform the input text
        text_vec = self.vectorizer.transform([text])

        # Make a prediction
        prediction = self.model.predict(text_vec)

        # Return a structured result as a dictionary with the boolean converted to int
        return {"isSpam": int(prediction[0] == 1)}  # Convert the boolean to int (1 or 0)


# Example usage
if __name__ == "__main__":
    # Initialize the spam detector
    spam_detector = SpamDetector()

    # If the model is not trained, we can train it (uncomment the following line)
    # spam_detector.train('spam_data.csv')

    # Make predictions
    example_text = "Congratulations! You've won a free gift card!"
    result = spam_detector.predict(example_text)
    print(f"Prediction for '{example_text}': {result}")

    example_text = "Can we schedule a meeting for next week?"
    result = spam_detector.predict(example_text)
    print(f"Prediction for '{example_text}': {result}")
