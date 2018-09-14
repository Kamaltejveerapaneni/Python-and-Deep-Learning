from collections import defaultdict
import random

items = [random.randint(0, 20) for x in range(15)]
print(items)
counter = defaultdict(lambda: 0)
for i in items:
    counter[i] += 1

item, amount = sorted(counter.items(), key=lambda x: x[1], reverse=True)[0]

print ('item %s is the most common with %s occurrances' % (item, amount))