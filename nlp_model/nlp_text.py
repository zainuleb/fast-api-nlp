import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('popular')

def preproc(str):

    # text = input()
    text = str
    # print(text)

    #convert text to lowercase
    text = text.lower()
    # print(text)

    #remove punctuations from the text using regex
    text = re.sub(r'[^\+\-\w\s]', '', text)
    # print(text)

    # #spelling correction using textblob
    # txtblob = TextBlob(text)
    # text = str(txtblob.correct())


    #tokenization nltk
    text_tokens = nltk.word_tokenize(text)
    # print(text_tokens)

    #remove stop words nltk
    stop_words = set(stopwords.words('english'))
    text_tokens_nostop = []

    for w in text_tokens:
        if w not in stop_words:
            text_tokens_nostop.append(w)

    # print(text_tokens_nostop)

    #stemming the words using PorterStemmer
    # ps = PorterStemmer()
    # stemm_text = []
    # for w in text_tokens_nostop:
    #     stemm_text.append(ps.stem(w))

    # print(stemm_text)

    #lemmatize the words using WordNet-Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemm_text = []
    for w in text_tokens_nostop:
        lemm_text.append(lemmatizer.lemmatize(w))

    # print (lemm_text)
    return (lemm_text)