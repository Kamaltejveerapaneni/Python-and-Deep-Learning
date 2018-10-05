import nltk
import re
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams, wordpunct_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
ps = PorterStemmer() # used as a variable to call Porterstemmmer
lemmatizer = WordNetLemmatizer() # used as a variable to call lemmatizer of word

my_list = []  # used to store the links
para =[] # used to store the line which are further stored in txt file
my_link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# our link which we want to print
link = requests.get(my_link)
# requesting the link
with open("output2.txt") as file:
    for line in file:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        print(urls)
# to clear the previous data
f = open("output2.txt", "w")
f.write("")
f.close()
obj = BeautifulSoup(link.content, "html.parser")
# print the title of the webpage
print(obj.title)

my_list.append(obj.find_all('a'))
# collecting data/links on to list

# goes through each  'a' to get the reference
for i in obj.find_all('a'):
    #print(i.get('href'))
    f = open("output2.txt", "a")
    para = str(i.get('href'))
    f.write(para.replace("/wiki/"," "))
    f.write("\n")
    f.close()

# reading the values from the txt file and reading as a line
f = open("output2.txt", "r",encoding="utf-8")
fileread = f.read()


senttokens = sent_tokenize(fileread) # sentence tokenizing
wordtokens = word_tokenize(fileread) # word tokenizing

# sentence tokenized printing
print("sentence  tokenized :")
print(senttokens)
print("--------------------------------------------------------")
# word tokenized printing
print("word tokenized :")
print(wordtokens)
print("--------------------------------------------------------")
#1.stemming of data
print("stemming:")
stemm =[]
for w in wordtokens:
    stemm.append(ps.stem(w))

print(stemm)
print("--------------------------------------------------------")
#2.Parts of speech
print("Part Of Speech:")


def process_content():
    try:
        for i in senttokens[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()

#3.lemmatizing the data
print("lemmatizing:")

lem=[]
for w in wordtokens:
    lem.append(lemmatizer.lemmatize(w))

print(lem)
print("--------------------------------------------------------")
#4.trigram the data
print("trigram")
print("")
sent = " i am studying in umkc which is a good university"
text = word_tokenize(sent)
trigram = ngrams(text,3)
for t in trigram:
    print(t)
print("--------------------------------------------------------")

#5.Named Entity Recognition of text
print("Named Entity Recognition:")

NER=[]
NER.append(ne_chunk(pos_tag(wordpunct_tokenize(str(senttokens)))))#nltk.ne_chunk returns a nested nltk.tree.Tree object so you would have to traverse the Tree object to get to the NEs.
#As you get a tree as a return value, I guess you want to pick those subtrees that are labeled with S
print(NER)



