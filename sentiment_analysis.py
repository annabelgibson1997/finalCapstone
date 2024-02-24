import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob # Spacy text blob helps with sentiment analysis

# implement a sentiment analysis model using spacy
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def clean_text(whole_review_data): # preprocess the data
    cleaned_reviews = {}
    for review in whole_review_data:
        doc = nlp(review)
        cleaned_text = ' '.join([token.text.lower() for token in doc if not token.is_stop and token.text.strip()])
        cleaned_reviews[review] = cleaned_text # removing stop words and converting text to lowercase
    return cleaned_reviews

# creating a function for sentiment analysis
def sentiment_analysis(cleaned_data):
    for key, value in cleaned_data.items():
        doc = nlp(value)
        polarity = doc._.blob.polarity

        # categorising the sentiment as positive, negative or neutral
        if polarity > 0.1:
            sentiment_category = "Positive"
        elif polarity < -0.1:
            sentiment_category = "Negative"
        else:
            sentiment_category = "Neutral"

        print(f"\nReview: {key}")
        print(f"Sentiment: {polarity}")
        print(f"Sentiment Category: {sentiment_category}")

# reading Amazon CSV file and removing rows with missing review text with dropna()
amazon_data = pd.read_csv("amazon_product_reviews.csv", sep=",")
amazon_data = amazon_data.dropna(subset=['reviews.text'])
reviews_data = amazon_data['reviews.text'].iloc[[0,22,232,4202,6272,24022,21748]]
sentiment_analysis(clean_text(reviews_data)) # testing the sentiment analysis function

# selecting two reviews for similarity comparison using indexing
my_review_of_choice_one = amazon_data['reviews.text'][22]
my_review_of_choice_two = amazon_data['reviews.text'][232] # chosen these because they both talk about batteries

# loading a different spacy model for similarity comparison
nlp = spacy.load('en_core_web_md')

def similarity(one, two): # calculating the similarity
    similarity_result = nlp(one).similarity(nlp(two))
    return(similarity_result)

print(f"\nReview One: {my_review_of_choice_one}") # showing the reviews before showing their similarity
print(f"\nReview Two: {my_review_of_choice_two}")
print(f"\nSimilarity: {similarity(my_review_of_choice_one, my_review_of_choice_two)}")
