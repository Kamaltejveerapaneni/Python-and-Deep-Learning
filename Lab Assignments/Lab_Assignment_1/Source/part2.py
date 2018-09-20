#consider first file as from a.txt
#consider second file as from b.txt
a = "a.txt"
b = "b.txt"

# first file list
aWordsList = []
# second file list
bWordsList = []

# Open the File and then split it and read each word
#first file words list in an array
with open(a) as f:
    aWordsList = f.read().split()

#second file words list in an array in lowercase
with open(b) as f:

    bWordsList = f.read().lower().split()


# Write access opening for first file
aOut = open(a, 'w')

# Here we loop the first file list and compare whether words in first file word  are there in second file
for aWord in aWordsList:
    if aWord.lower() not in bWordsList:
        aOut.write(aWord+" ")#Write to the file if first file word cannot be seen in second file