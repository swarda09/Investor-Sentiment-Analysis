# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:44:01 2024

@author: Sangeeta
"""

import pandas as pd
import re

# Load the CSV file
df = pd.read_csv("Data_Scraped - Metadata.csv")

# Function to extract dates from text using regex
def extract_published_date(text):
    # Date pattern to match day-month-year or similar formats (e.g., '31 Dec 2020')
    date_pattern = r'(\d{1,2} \w{3} \d{4})'
    match = re.search(date_pattern, text)
    if match:
        return match.group(0)
    return None

# Apply the function to the 'text' column
df['Published Date'] = df['text'].apply(extract_published_date)

# Display the result with published dates
print(df[['text', 'Published Date']].head())
print()
print(df[['text', 'Published Date']].isnull().sum())
print()
#pip beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup

# Function to scrape data from the given URL
def scrape_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.title.get_text() if soup.title else "No title available"

        # Extract article text (this might vary by site structure)
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])

        return title, article_text
    except Exception as e:
        return "Error", "Could not retrieve the content"

# Apply the function to the 'url' column and create new columns
df['Title'], df['Text'] = zip(*df['url'].apply(scrape_url))

# Display the updated dataframe with Title and Text columns
print(df[['url', 'Title', 'Text']].head())

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

# Function to generate summary (basic word frequency summary)
def generate_summary(text, n=5):
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    most_common = Counter(filtered_words).most_common(n)
    summary = ' '.join([word for word, count in most_common])
    return summary

# Apply the function to the 'Text' column
df['Summary'] = df['Text'].apply(generate_summary)

# Display the result with summary
print(df[['Text', 'Summary']].head())

df.to_csv('final_output.csv', index=False)

