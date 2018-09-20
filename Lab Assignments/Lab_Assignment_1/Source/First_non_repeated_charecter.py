text=input("enter a text:")
print(f"text:{text}")

dict={}
for c in text:
    if c.isalpha():
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1


first = next((x for x in dict if dict[x] == 1))
print(f"First non repeating char:{first}")