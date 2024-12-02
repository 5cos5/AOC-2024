import numpy as np
import pandas as pd

# Part 1
data = np.array(pd.read_csv('data.csv'))
# data = np.array(pd.read_csv('data_test.csv'))

list1_sorted = np.sort(data[:,0])
list2_sorted = np.sort(data[:,1])

diff = np.abs(list1_sorted-list2_sorted)

print ("Total Difference is:",sum(diff))

# Part 2
list1 = data[:,0]
list2 = data[:,1]

unique_in_1, counts_in_1 = np.unique(list1, return_counts=True)


# print (unique)
# print (counts)
score = 0
for idx, num in enumerate(unique_in_1):
    counts_in_2 = (list2 == num).sum()
    # print ('Unique NUmber:',num)
    # print (counts_in_2)
    score+= num*counts_in_2*counts_in_1[idx]

print ("Score:",score)
