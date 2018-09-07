import re
a=input("The input Sequence is:")
print(a)
print("The individual codon sequences are",re.findall(r'.{1,3}',a,re.DOTALL))
b= re.findall(r'.{1,3}',a,re.DOTALL)
#SPLItting codons works upto here I.E WORKING WITH REGU;AR EXPRESSIONS
