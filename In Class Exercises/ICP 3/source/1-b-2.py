import csv
from collections import Counter

dna_dict = {}
with open(r"C:\Users\kamal\PycharmProjects\sample3\codon.tsv") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    try:
      dna_dict[row[0]] = row[1]
    except:
      pass
while True:
    a = input("The input Sequence is:")
    print(a)
    print("The individual codon sequences are", re.findall(r'.{1,3}', a, re.DOTALL))
    b = re.findall(r'.{1,3}', a, re.DOTALL)
  print("the individual codon sequence is: ", codons)
try:
    codon_names = list(map(lambda x: dna_dict[x], codons))
    break
  except:
    print("not present enter another ")

name_counts = Counter(codon_names)
print("the names and count of codons: ", name_counts)