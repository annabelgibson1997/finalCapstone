# finalCapstone

**Project Title: Sentiment Analysis**

## Description

This project implements sentiment analysis on Amazon product reviews using spaCy and spaCyTextBlob. It includes a sentiment analysis model and a similarity comparison function.

## Table of Contents

- [Installation]
- [Usage](#usage)
- [Credits](#credits)

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/your-repo.git](https://github.com/annabelgibson1997/finalCapstone)
   cd finalCapstone

3. Install dependencies:

pip install pandas spacy spacytextblob

3. Download spaCy model:

python -m spacy download en_core_web_sm

4. Run the script:

python sentiment_analysis.py

## Usage

Import the necessary libraries:

import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

Load the spaCy model and add the spaCyTextBlob pipeline:

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

Clean and preprocess the review data:

cleaned_reviews = clean_text(whole_review_data)

Perform sentiment analysis:

sentiment_analysis(cleaned_reviews)

<img width="492" alt="Screenshot 2024-02-24 at 17 27 16" src="https://github.com/annabelgibson1997/finalCapstone/assets/153768779/fff478a7-f529-4626-b607-c62842a59ee9">

<img width="688" alt="Screenshot 2024-02-24 at 17 29 06" src="https://github.com/annabelgibson1997/finalCapstone/assets/153768779/812374a9-7a6b-4c59-a760-e194259651a9">

Compare the similarity of two reviews:

similarity_result = similarity(review_one, review_two)

<img width="498" alt="Screenshot 2024-02-24 at 17 27 25" src="https://github.com/annabelgibson1997/finalCapstone/assets/153768779/661dee71-f154-4c41-9c60-4498c0af34a8">

<img width="836" alt="Screenshot 2024-02-24 at 17 29 16" src="https://github.com/annabelgibson1997/finalCapstone/assets/153768779/03efa9da-6192-4069-bcb2-ece8747cf901">

## Credits

Author: Annabel Gibson https://github.com/annabelgibson1997
