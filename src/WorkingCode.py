# Import necessary spacy and os packages to parse through data

import spacy
import os

# Add tokenizer so that spacy 
nlp = spacy.load("en_core_web_sm")

# 

# Parsing function

def text_parsing(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        doc = nlp(text)
        return doc

# Tensorizer - this gives words parts of speech

