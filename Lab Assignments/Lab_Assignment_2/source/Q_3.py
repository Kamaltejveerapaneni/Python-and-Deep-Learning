import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams
from nltk import FreqDist
import collections


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
ps = PorterStemmer() # used as a variable to call Porterstemmmer
lemmatizer = WordNetLemmatizer() # used as a variable to call lemmatizer of word

f = open("input.txt", "r",encoding="utf-8")
fileread = f.read()



senttokens = sent_tokenize(fileread) #sentence tokenizing
wordtokens = word_tokenize(fileread) # word tokenizing
print(wordtokens)
# lemmatizing the data
print("lemmatizing:")

lem=[]
for w in wordtokens:
    lem.append(lemmatizer.lemmatize(w))

print(lem)


# performing Bigram on the  Lemmatizer Output
print("Bigrams :\n")
bigramsOtpt = []
for big in ngrams(wordtokens, 2):
    # Fetching Bigrams using 'ngrams' method and Iterating it and appending it to list
    bigramsOtpt.append(big)
print(bigramsOtpt)

# BiGram- Word Frequency
# Using bigramOutput fetch the WordFreq Details
wordFreq = FreqDist(bigramsOtpt)
# Most commoon bigrams
mostCommon = wordFreq.most_common()
print("BiGrams Frequency in asecing order : \n", mostCommon)
# First 5 bigrams
First5 = wordFreq.most_common(5)
print("First 5 Bigrams : \n", First5)

# Creating an Array to append the sentence
cncatArray = []
# Iterating the Sentences
for s in senttokens:
    # Iterating all the bigrams
    for a, b in bigramsOtpt:#iterating the firsts 5 most bigrams from all the bigrams BiGrams
        for ((c, d), length) in First5: # Comparing the each with the first 5 most repeated bigrams
            if(a, b == c, d):
                cncatArray.append(s)

print("Concatenated Array : ",cncatArray)
print("Maximum of Concatenated Array : ", max(cncatArray))

