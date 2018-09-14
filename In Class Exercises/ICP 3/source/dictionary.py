import csv
from collections import Counter
dict_1 = {}
with open(r"C:\Users\kamal\Documents\Github\Python-and-Deep-Learning\In Class Exercises\ICP 3\source\codon.tsv") as infile:
    reader = csv.reader(infile, delimiter='\t')
    for rows in reader:
        dict_1[rows[0]] = rows[1]
x = input("enter the sequence")
i = 0
list_1 = []
while i < len(x):
    list_1.append(x[i:i+3])
    i = i+3
i=0
print(list_1)
list_2=[]
while i<len(list_1):
    x=(dict_1[list_1[i]])
    list_2.append(x)
    i = i + 1
print(Counter(list_2))