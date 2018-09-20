str1 = []
with open("C://Users//matur//Desktop//UMKC//python_lee//Lab_Assignment_1//a.txt", "r") as f:
  for line in f:
    str1.append(line.strip().lower())

s1=list(str1[0].split(" "))

print(s1)
str2 = []
with open("C://Users//matur//Desktop//UMKC//python_lee//Lab_Assignment_1//b.txt", "r") as f:
  for line in f:
    str2.append(line.strip())

s2=list(str2[0].split(" "))
new_str= " "

print(s2)
for i in s1:
    for j in s2:
        if i == j:
            ind = s1.index(i)
            s1[ind] = ""

print(' '.join(s1))