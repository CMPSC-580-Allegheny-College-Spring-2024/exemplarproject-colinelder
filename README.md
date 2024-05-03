[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)
# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

## GitHub Handle: colinelder

## Name: Colin Elder

## Major: Data Science, Economics

## Project Name: Colin's Fact Finder

---

## Overview

Colin's fact finder is an exciting new development in the way that people are able to access new information and verify what they already know about scientific information. Through an interactive streamlit platform and backed by a powerful Python system, users are able to input a scientific fact and instantly have it verified or rejected. The program does this by parsing through a large corpus of scholarly articles and returning the article from which it was found in. 

The fact finder program is able to complete this task by utilizing text matching techniques within the fuzzy library and text parsing techniques to move through the vast corpus. The main goal of this project was to provide users with a trustworthy tool for verifying their questions by utilizing well-established scholarly articles. This technique ensures that the data that is being checked against is valid and improves the accuracy of the program. Additionally, it encourages the reader to look more into said articles and read more scholarly publications. Ultimately, it is the vast amount of knowledge found in these publications that allow the fact finder to properly work and operate.

The significance of this project lies in the relevancy this is the increase in use of machine learning and text matching techniques. The prevalance of artificial intelligence and its capabilities has skyrocketed in recent times, and machine learning and text matching go hand in hand with that. This project is able to demonstrate the usefulness and impressive capabilities of these techniques as well as how they are able to be implemented properly.

## Literature Review

The first book that I reviewed for this project was Text Analytics with Python: A Practitioner's Guide to Natural Language Processing. This book provided me with a lot of backround knowledge on what natural language processing was and how it works. This book helped readers connect their ideal project to natural language processing and realize how it can benefit them. Additionally, it addresses the current limitations and work being done to improve text analysis with machine learning and natural language processing. 

From this, the next article reviewed the ways that a user can begin to implement natural language processing within python. This book was titled "Natural Language Processing with Python- A Practical Introduction. This demonstrated many ways and libraries that the user could use to start analyzing text in python. This helped to narrow down which and figure out which solution would be best for this artifact.

The goal of the next article was to review a specific library more in depth so that it could be implemented best. This turned out to be the ```fuzzywuzzy``` library. This article included ways to install the library, how to run it, and a more in depth view on how it works/how to best implement it in code.

The final article reviewed delt with the user interface, which was ```streamlit```. This was one that was suggested by the professor at the beginning of the project, so this article supplement the information already given to us and provided extra information about how it works. This article helped to design and run the interface properly so that it was user friendly and implemented the code properly with it.

## Methods

The first step that I took to complete this project was completing primary research on the project. This included looking into different techniques for text analysis and the different possible directions that I could move forward in. I also looked into what mediums I could use for the user end of the program and what interface would be best to work with. Finally, I looked at relevant previous fact checking programs. 

The next step for this project was finding relevant data to reference in order to verify the user's input. Fortunately, we had data that was provided to us by professor Bonham-Carter that was immensely valuable. Unfortunately however, this large corpus of data exceeded github's repository size limitations. Therefore the full dataset is not able to be found in the github repository. There is a small example of the data found in the data folder, as well as in the data ReadME. 

From this point, I was able to start implementing my artifact. The first steps that I took to do this was verifying that my program was able to parse through each text file successfully. I started by creating the path to my data and then appended each text file to a list it moved through them.

The next step that I took was implementing the user interface/dashboard for the program. After some research I settled on streamlit for this aspect of the artifact. I decided on this because I was able to find a lot of valuable information about it as well as valuable tutorials and demonstrations.

Following this, I was able to start working on the fact checking implementation and text analysis. To find the best way to go about this, I reviewed articles that outlined various possible libraries and techniques that I could use for this implementation. One library in particular that seemed to be a very viable option was the ```Spacy``` library. While this seemed like a good option at the time, after a lot of valuable discussion in class I turned to a different library that other students had found more success with. This was the ```fuzzywuzzy```. This library allowed the programmer to implement a similarity threshold which allowed for a better range of text matching for the program. This ensures that the question inputted does not have to perfectly match the text file, but rather meet a quota for similarity.

The last thing that I did to verify the usability was manual experimentation for the program. This involves going into the streamlit dashboard myself and asking questions as if I were a user. However, I already knew the answer to my facts and where to find them in the text files. From this I could verify that proper output was being produced. Additionally, I quickly added a print statement in my parsing function so that I could verify that each text file was in fact being parsed through. This print statement printed the name of each file as it was appended to the list.


## Using the Artifact


The first step in making sure that you can run the fact finder is that you make sure that you have the right data and the correct path to it. To read more about the data, see the data folder located within the github repository. To ensure that the correct path to the data is being used, ensure that the data are all .txt files and adjust the following line in the code as necessary.

```data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Jsem_Data')```

Beyond this, the user must verify that they have correctly installed all of the proper libraries. There are three libraries needed for this project. They are ```os```, ```fuzzywuzzy```, and ```streamlit```. To install these run the following commands- 

```pip install streamlit```
```pip install os```
```pip install fuzzywuzzy```

From there, the program is ready to run! All the user needs to do is run the following command in the terminal, just be sure that you are located in the proper directory location before running the command. This is the ```src``` directory. The command is as follows:

```streamlit run workingcode.py```

After this is ran, the article will automatically transport you to the streamlit dashboard where the user can input whatever fact they want.


## Results and Outcomes

One of the first tests that was ran in order to verify that this artifact was working properly was printing out the list of files as they were being parsed through in the code. By viewing the print statement, it was able to be verified that each article was being parsed through one at a time.

The ultimate outcome of this program is a true or false value being returned, as well as the file in which it was found. This allows users to verify their questions with trustworthy sources as well as further their knowledge by reading the scholarly source that their question was answered in.

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
