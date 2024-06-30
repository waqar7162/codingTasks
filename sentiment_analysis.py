import spacy
from textblob import TextBlob
import pandas as pd
import os

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Load the dataset
file_path = r"C:\Users\waqar\OneDrive\Desktop\CoGrammer\T26-Task_26 (Natural Language Processing with SpaCy)\amazon_product_reviews.csv"
print(f"Loading data from: {file_path}")
df = pd.read_csv(file_path)

# Function to preprocess the text
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

# Apply preprocessing to the reviews
df['cleaned_reviews'] = df['reviews.text'].apply(lambda x: preprocess_text(str(x)))

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Apply sentiment analysis to the cleaned reviews
df['sentiment'] = df['cleaned_reviews'].apply(lambda x: analyze_sentiment(x))

# Save the results to a new CSV file
output_file_path = r"C:\Users\waqar\OneDrive\Desktop\CoGrammer\T26-Task_26 (Natural Language Processing with SpaCy)\amazon_product_reviews_with_sentiment.csv"
print(f"Attempting to save results to: {output_file_path}")

try:
    df.to_csv(output_file_path, index=False)
    print(f"Sentiment analysis completed and results saved to '{output_file_path}'")
except Exception as e:
    print(f"Error saving file: {e}")

# Verify the output path
if os.path.exists(output_file_path):
    print(f"File successfully created at: {output_file_path}")
else:
    print(f"Failed to create file at: {output_file_path}")

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")
