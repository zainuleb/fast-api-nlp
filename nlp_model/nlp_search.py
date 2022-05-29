import speech_recognition as sr
# from googletrans import Translator
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer 

op = '''Choose data input:
1 - Audio
2 - Text'''
print(op)
x = input()


if (x=='1'):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        text = r.recognize_google(audio_text)
        # text = r.recognize_google(audio_text, language="ur-PK")
        # translator = Translator()
        # result = translator.translate(text, src='ur')
        # text = result.text
        try:
            print("Text: "+text)
        except:
             print("Sorry, I did not get that")

        #tokenization nltk
        text_tokens = nltk.word_tokenize(text)
        print(text_tokens)

        #remove stop words nltk
        stop_words = set(stopwords.words('english'))
        text_tokens_nostop = []

        for w in text_tokens:
            if w not in stop_words:
                text_tokens_nostop.append(w)

        print(text_tokens_nostop)

elif (x=='2'):
    print("Enter query:")
    text = input()
    # print(text)

    #convert text to lowercase
    text = text.lower()
    # print(text)

    #remove punctuations from the text using regex
    text = re.sub(r'[^\+\-\w\s]', '', text)
    # print(text)

    #spelling correction using textblob
    txtblob = TextBlob(text)
    text = txtblob.correct()
    
    #tokenization nltk
    text_tokens = nltk.word_tokenize(text)
    print(text_tokens)

    #remove stop words nltk
    stop_words = set(stopwords.words('english'))
    text_tokens_nostop = []

    for w in text_tokens:
        if w not in stop_words:
            text_tokens_nostop.append(w)

    print(text_tokens_nostop)

    #lemmatize the words using WordNet-Lemmatizer
    lemmatizer = WordNetLemmatizer()
    for i in text_tokens_nostop:
        i = lemmatizer.lemmatize(i)

    print(text_tokens_nostop)
