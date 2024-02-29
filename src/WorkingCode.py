# Import necessary spacy and os packages to parse through data and read text

import spacy
import os
import re
# Import streamlit, which will be used as the interface for users
import streamlit as st

# Add tokenizer so that spacy can assign vectors to words
nlp = spacy.load("en_core_web_sm")

# define file path to text directories
data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Jsem_Data')

# Creates empty list for text file paths
text_path = []

# Function to remove any non letter characters in the text
def remove_non_letters(data):
    # This uses regular expression to remove non-letter characters from text files
    return re.sub(r'[^a-zA-Z]', '', data)

# Program needs to iterate through files

for filename in os.listdir(data_path):
        file_path = os.path.join(data_path, filename)
        with open(file_path, 'r') as file:
            # Process content of the file here
            content = file.read()
            # Example: print the filename
            print(f"File: {filename}")

# fact checking function
def fact_checker(input,data):
     # processing text file
     doc = nlp(data)
     # Processing user input
     doc = nlp(input)


# Streamlit interface

st.title("Fact Checking Program")
fact_input = st.text_input("Enter the fact you want to check:")

if st.button("Check Fact"):
    if fact_input:
        found, found_in_files = fact_check(fact_input)
        if found:
            st.success("The fact is true.")
            st.write(f"Found in file(s): {', '.join(found_in_files)}")
        else:
            st.error("The fact is false.")
    else:
        st.warning("Please enter a fact to check.")

# Parsing function

#def text_parsing(file_path):
 #   with open(file_path, "r", encoding="utf-8") as file:
  #      text = file.read()
   #     doc = nlp(text)
    #    return doc

# Tensorizer - this gives words parts of speech

