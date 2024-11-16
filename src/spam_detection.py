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
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = LogisticRegression()
        self.vectorizer_path = r'src\vectorizer.pkl'
        self.model_path = r'src\spam_model.pkl'

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
        X_vec = self.vectorizer.fit_transform(X)

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

        # Train the model
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
            str: "Spam" if classified as spam, otherwise "Not Spam".
        """
        # Load the vectorizer and model
        if not os.path.exists(self.vectorizer_path) or not os.path.exists(self.model_path):
            raise FileNotFoundError("Model or vectorizer file not found. Please train the model first.")

        with open(self.vectorizer_path, 'rb') as vec_file:
            self.vectorizer = joblib.load(vec_file)
        with open(self.model_path, 'rb') as model_file:
            self.model = joblib.load(model_file)

        # Transform the input text
        text_vec = self.vectorizer.transform([text])

        # Make a prediction
        prediction = self.model.predict(text_vec)
        return "Spam" if prediction[0] == 1 else "Not Spam"


# Example usage
if __name__ == "__main__":
    # Initialize the spam detector
    spam_detector = SpamDetector()

    # Train the model
    data_path = 'spam_data.csv'  # Path to your dataset
    spam_detector.train(data_path)

    # Make predictions
    example_text = "Congratulations! You've won a free gift card!"
    print(f"Prediction for '{example_text}': {spam_detector.predict(example_text)}")

    example_text = "Can we schedule a meeting for next week?"
    print(f"Prediction for '{example_text}': {spam_detector.predict(example_text)}")
