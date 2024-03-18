from fuzzywuzzy import fuzz
import os
import streamlit as st

# Define file path to text directories. 
data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Jsem_Data')

# Function to read and preprocess text files
def preprocess_files(directory):
    texts = {}
    for filename in os.listdir(data_path):
        file_path = os.path.join(data_path, filename)
        if filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Store content with filename as key
                texts[filename] = content
    return texts


# Fact-checking function
def fact_checker(input_fact, texts, threshold=75):
    found_in_files = []
    for filename, content in texts.items():
        similarity_score = fuzz.partial_ratio(input_fact.lower(), content.lower())
        if similarity_score >= threshold:
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

