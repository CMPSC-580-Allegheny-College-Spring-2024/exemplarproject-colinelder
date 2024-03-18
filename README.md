[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)
# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: colinelder

## Name: Colin Elder

## Major: Data Science

## Project Name: Colin's Fact Finder

---

## Overview

Colin's fact finder is an exciting new development in the way that people are able to access new information and verify what they already know about scientific information. Through an interactive streamlit platform and backed by a powerful Python system, users are able to input a scientific fact and instantly have it verified or rejected. The program does this by parsing through a large corpus of scholarly articles and returning the article from which it was found in. 

The fact finder program is able to complete this task by utilizing text matching techniques within the fuzzy library and text parsing techniques to move through the vast corpus. The main goal of this project was to provide users with a trustworthy tool for verifying their questions by utilizing well-established scholarly articles. This technique ensures that the data that is being checked against is valid and improves the accuracy of the program. Additionally, it encourages the reader to look more into said articles and read more scholarly publications. Ultimately, it is the vast amount of knowledge found in these publications that allow the fact finder to properly work and operate.

The significance of this project lies in the relevancy this is the increase in use of machine learning and text matching techniques. The prevalance of artificial intelligence and its capabilities has skyrocketed in recent times, and machine learning and text matching go hand in hand with that. This project is able to demonstrate the usefulness and impressive capabilities of these techniques as well as how they are able to be implemented properly.

## Literature Review

TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.

## Methods

The first step that I took to complete this project was completing primary research on the project. This included looking into different techniques for text analysis and the different possible directions that I could move forward in. I also looked into what mediums I could use for the user end of the program and what interface would be best to work with. Finally, I looked at relevant previous fact checking programs. 

The next step for this project was finding relevant data to reference in order to verify the user's input. Fortunately, we had data that was provided to us by professor Bonham-Carter that was immensely valuable. Unfortunately however, this large corpus of data exceeded github's repository size limitations. Therefore the full dataset is not able to be found in the github repository. There is a small example of the data found in the data folder, as well as in the data ReadME. 

From this point, I was able to start implementing my artifact. The first steps that I took to do this was verifying that my program was able to parse through each text file successfully. I started by creating the path to my data and then appended each text file to a list it moved through them.

The next step that I took was implementing the user interface/dashboard for the program. After some research I settled on streamlit for this aspect of the artifact. I decided on this because I was able to find a lot of valuable information about it as well as valuable tutorials and demonstrations.

Following this, I was able to start working on the fact checking implementation and text analysis. To find the best way to go about this, I reviewed articles that outlined various possible libraries and techniques that I could use for this implementation. One library in particular that seemed to be a very viable option was the ```Spacy``` library. While this seemed like a good option at the time, after a lot of valuable discussion in class I turned to a different library that other students had found more success with. This was the ```fuzzywuzzy```. This library allowed the programmer to implement a "similarity score" which allowed for a better range of text matching for the program. This ensures that the question inputted does not have to perfectly match the text file, but rather meet a quota for similarity.

The last thing that I did to verify the usability was manual experimentation for the program. This involves going into the streamlit dashboard myself and asking questions as if I were a user. However, I already knew the answer to my facts and where to find them in the text files. From this I could verify that proper output was being produced. Additionally, I quickly added a print statement in my parsing function so that I could verify that each text file was in fact being parsed through. This print statement printed the name of each file as it was appended to the list.


TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

## Using the Artifact

TODO: The result of your work will be the delivery of some type of artifact which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). To allow the user to experience and execute your artifact, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
