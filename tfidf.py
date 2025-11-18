import re
import math

def read_stopwords(filename='stopwords.txt'):
    try:
        with open(filename, 'r') as f:
            stopwords = set(word.strip().lower() for word in f.readlines())
        return stopwords
    except FileNotFoundError:
        print(f"Stopwords file '{filename}' not found.")
        return set()

# Clean the input text by removing links, special characters, extra spaces, and converting to lowercase
def clean_text(text):
    # Removing website links
    text = re.sub(r'https?://\S+', "", text)
    
    # Removing all character that are not words(sequences of letters, digits and underscores) or whitespaces
    text = re.sub(r'[^\w\s]', '', text)
    
    # Removing extra whitespaces
    text = re.sub(r'\s+', ' ', text)
    
    # Converting to lowercase and stripping of leading/trailing whitespaces
    text = text.lower().strip()
    
    return text

# Removing stopwords for text
def remove_stopwords(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

# Applying stemming and lemmatization to words
def stem_word(text):
    words = text.split()
    stemmed_words = []
    
    for word in words:
        if word.endswith('ing') and len(word) > 3:
            word = word[:-3]
        elif word.endswith('ly') and len(word) > 2:
            word = word[:-2]
        elif word.endswith('ment') and len(word) > 4:
            word = word[:-4]
        
        stemmed_words.append(word)
    
    return ' '.join(stemmed_words)

# Preprocess the document by applying cleaning, stopword removal, and stemming
def preprocess_document(input_file, output_file, stopwords):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return None
    
    text = clean_text(text)
    
    text = remove_stopwords(text, stopwords)
    
    text = stem_word(text)
    
    text = remove_stopwords(text, stopwords)
    
    if not output_file.startswith('preproc_'):
        output_file = 'preproc_' + output_file
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    return text

# Computing word frequencies for each word in text
def compute_word_frequencies(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Comptuing the tf(Term Freqienuency) for each word in text
def compute_tf(word_freq, total_words):
    if total_words == 0:
        return {}
    tf = {}
    for word, count in word_freq.items():
        tf[word] = count / total_words
    return tf

# Computing the idf(Inverse Document Frequency) for each word accross all documents
def compute_idf(document_word_freq, total_docs):
    word_doc_count = {}
    for doc_freq in document_word_freq:
        for word in doc_freq.keys():
            word_doc_count[word] = word_doc_count.get(word, 0) + 1
    
    idf = {}
    for word, doc_count in word_doc_count.items():
        idf[word] = math.log(total_docs / doc_count) + 1
    
    return idf

# Computing tf-idf scores for all documents
def compute_tfidf(doc_files, preprocessed_texts):
    documents_word_freq = []
    total_words_per_doc = []
    
    for text in preprocessed_texts:
        if text is not None:
            word_freq = compute_word_frequencies(text)
            documents_word_freq.append(word_freq)
            total_words_per_doc.append(sum(word_freq.values()))
        else:
            documents_word_freq.append({})
            total_words_per_doc.append(0)
    
    idf = compute_idf(documents_word_freq, len(doc_files))
    
    for i, (doc_file, word_freq) in enumerate(zip(doc_files, documents_word_freq)):
        if not word_freq:
            with open('tfdif_' + doc_file, 'w', encoding='utf-8') as f:
                f.write("[]")
            continue
        
        tf = compute_tf(word_freq, total_words_per_doc[i])
        
        tfidf_scores = {}
        
        for word in word_freq.keys():
            tfidf_scores[word] = round(tf[word] * idf[word], 2)
        
        sorted_tfidf = sorted(tfidf_scores.items(), key=lambda x: (-x[1], x[0]))
        
        top_5 = sorted_tfidf[:5]
        
        output_file = 'tfidf_' + doc_file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(top_5))

with open('tfidf_docs.txt', 'r') as f:
    doc_files = [line.strip() for line in f.readlines() if line.strip()]

stopwords = read_stopwords()

preprocessed_texts = []
for doc_file in doc_files:
    output_file = 'preproc_' + doc_file
    preprocessed_text = preprocess_document(doc_file, output_file, stopwords)
    preprocessed_texts.append(preprocessed_text)

compute_tfidf(doc_files, preprocessed_texts)