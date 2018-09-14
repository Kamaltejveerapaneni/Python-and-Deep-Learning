#use of mode() function
# mode() function a sub-set of the statistics module
# We need to import statistics module before doing any work
import statistics
from statistics import mode
import numpy as np #we import numpy as np


randnums = np.random.randint(0,21,15)#create a variable names randnums and set it to np.random.rand
#here 0 is inclusive 21 is exclusive



print(randnums)# Printing out the entire list
print("Most repeated value is:",statistics.mode(randnums))# Printing out mode of given data-set



'''

from collections import Counter
import numpy as np #we import numpy as np


randnums = np.random.randint(0,21,15)#create a variable names randnums and set it to np.random.rand
#here 0 is inclusive 21 is exclusive

print(randnums)

freq = Counter(randnums)
freq2 = freq.most_common()#all unique values and counts returned
freq3 = freq.most_common(1)# most frequent value is returned
print(freq3)

'''