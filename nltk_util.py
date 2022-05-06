
import nltk


#This is to be used once so that the package can use tokenization assets
#nltk.download('punkt')  

# There are many more stemmers ...we are using the PorterStemmer here
from nltk.stem.porter import PorterStemmer  

# Created our PorterStemmer for stemming
stemmer=PorterStemmer() 

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    pass

a="How is the cake shop?"
print(a)

a=tokenize(a)
print(a)

