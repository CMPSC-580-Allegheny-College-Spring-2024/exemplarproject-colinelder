# Import necessary spacy and os packages to parse through data

import spacy
import os
import re
import streamlit as st

# Add tokenizer so that spacy can assign vectors to words
nlp = spacy.load("en_core_web_sm")

# define file path to text directories
data_path = os.path.join(os.path.dirname(__file__), '..', '..','exemplar_data')

# Creates empty list for text file paths
text_path = []

# Function to remove any non letter characters in the text
def remove_non_letters(text):
    # This uses regular expression to remove non-letter characters from text files
    return re.sub(r'[^a-zA-Z]', '', text)

# Program needs to iterate through files

for filename in os.listdir(data_path):
        file_path = os.path.join(data_path, filename)
        with open(file_path, 'r') as file:
            # Process content of the file here
            content = file.read()
            # Example: print the filename
            print(f"File: {filename}")

# Parsing function

def text_parsing(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        doc = nlp(text)
        return doc

# Tensorizer - this gives words parts of speech

