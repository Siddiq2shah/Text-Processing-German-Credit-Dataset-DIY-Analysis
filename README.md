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
