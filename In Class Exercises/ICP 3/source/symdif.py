first={"1","2","4","5"}
second={"1","2"}

add=first.union(second)
print("Union of first and second sets:",add)

common=first.intersection(second)
print("Intersection of two sets",common)

symdif=first.difference(second)
print("Symmetric difference between two sets is:",symdif)

