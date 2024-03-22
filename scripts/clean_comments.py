import pandas as pd
import os
import spacy
import re
import nltk
from nltk.corpus import stopwords

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Download NLTK stop words
nltk.download("stopwords")


def clean_text(text):
    # Remove URLs
    text = re.sub(r"https?:\/\/.*[\r\n]*", "", text)
    # Remove emojis and special characters
    text = re.sub(r"[^\w\s]", "", text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = text.split()
    filtered_words = [word for word in tokens if word not in stop_words]
    text = " ".join(filtered_words)
    return text


def advanced_clean_text(text):
    """Clean text using spaCy for lemmatization and stopword removal."""
    doc = nlp(text)
    lemmatized = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized


def main():
    # Assume the raw comments are stored in 'data/raw_comments.csv'
    df = pd.read_csv("data/raw_comments.csv")

    # Perform initial cleaning
    df["cleaned_comment"] = df["comment"].apply(clean_text)

    # Perform advanced cleaning
    df["cleaned_comment"] = df["cleaned_comment"].apply(advanced_clean_text)

    # Save the cleaned comments
    output_filename = "data/cleaned_comments.csv"
    df[["cleaned_comment"]].to_csv(output_filename, index=False)
    print(f"Cleaned comments saved to {output_filename}")


if __name__ == "__main__":
    main()
