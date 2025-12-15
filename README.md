Text Processing, German Credit Dataset, DIY Analysis  

## Overview
This repository implements three related data projects:
1. **Text Processing & TF–IDF** – a small NLP pipeline that cleans raw text documents, removes stopwords, applies simple stemming rules, and computes TF–IDF scores.
2. **German Credit Dataset Analysis** – preprocessing, exploratory analysis, and visualizations on the classic German Credit CSV file using pandas.
3. **DIY Dataset Project** – a full data-cleaning pipeline, custom analyses, and visualizations on a public CSV dataset of my choice.

---

## Project Structure

```text
.
├── tfidf.py                  # Problem 1: text processing + TF–IDF
├── tfidf_docs.txt            # List of input text files for TF–IDF
├── stopwords.txt             # Stopword list used in preprocessing
│
├── german_credit.ipynb       # Problem 2: German Credit preprocessing, analysis, plots
├── GermanCredit.csv          # German Credit dataset (1,000 records)
│
├── diy_dataset.ipynb         # Problem 3: DIY dataset cleaning, analysis, visualizations
├── diy_dataset.csv           # Cleaned DIY dataset saved after preprocessing

Text Processing & TF-IDF (tfidf.py)

Read raw text documents listed in a control file

Loaded and applied a stopword list for filtering common terms

Cleaned text by removing URLs, punctuation, extra whitespace, and normalizing case

Applied rule-based stemming to reduce words to root forms

Computed word frequencies per document

Calculated term frequency (TF) and inverse document frequency (IDF) manually

Generated TF-IDF scores without using NLP libraries

Ranked terms by importance and saved the top 5 keywords per document

Output cleaned text files and TF-IDF result files automatically

German Credit Dataset Analysis (german_credit.ipynb)

Loaded the German Credit CSV dataset into pandas

Cleaned and preprocessed numerical and categorical features

Performed exploratory data analysis (EDA)

Visualized distributions and relationships between credit variables

Identified patterns related to credit risk and borrower characteristics

Prepared the dataset for downstream statistical or ML analysis

DIY Dataset Cleaning & Analysis (diy_dataset.ipynb)

Loaded a self-selected public CSV dataset

Identified missing, inconsistent, or malformed data

Applied custom cleaning and transformation logic

Conducted exploratory analysis and visualizations

Generated insights specific to the chosen dataset

Saved a cleaned version of the dataset for reuse
