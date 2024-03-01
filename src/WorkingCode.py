import spacy
import os
import re
import streamlit as st

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Define file path to text directories. 
data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Jsem_Data')

# Function to clean text data
def remove_non_letters(data):
    # Retain spaces and letters for readability
    return re.sub(r'[^a-zA-Z\s]', '', data)

# Function to read and preprocess text files
def preprocess_files(directory):
    texts = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.txt'):
        # Appends the name of the file to the list instead of txt
            file_path.append(filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                cleaned_content = remove_non_letters(content)
                texts[filename] = cleaned_content
    return texts


# Fact-checking function
def fact_checker(input_fact, texts, threshhold=75):
    found_in_files = []
    for filename, content in texts.items():
        if input_fact.lower() in content.lower():
            found_in_files.append(filename)
    return found_in_files


# Load and preprocess the text data
texts = preprocess_files(data_path)

# Streamlit interface
st.title("Colin's Science Fact Checking Program")
fact_input = st.text_input(" Please enter the fact you want to check:")

if st.button("Check Fact"):
    if fact_input:
        found_in_files = fact_checker(fact_input, texts)
        if found_in_files:
            st.success("The fact is true!")
            st.write(f"Found in file(s): {', '.join(found_in_files)}")
        else:
            st.error("The fact is false :(")
    else:
        st.warning("Please enter a fact to check.")

