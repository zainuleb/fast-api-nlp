import speech_recognition as sr
from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
    
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