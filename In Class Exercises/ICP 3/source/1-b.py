import csv
import re
from collections import Counter

codict = {}
with open("C:\\Users\kamal\PycharmProjects\sample3\codon.tsv") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for cols in reader:
    codict[cols[0]] = cols[1]
  sequence = input(" enter the input sequence: ")

  codons = (re.findall(r'.{1,3}', sequence, re.DOTALL))
  print("the individual codon sequence is: ", codons)
  codon_names = list(map(lambda x: codict[x], codons))
name_counts = (codon_names)
print("the names and count of codons: ", Counter(name_counts))