import numpy as np
import pandas as pd

with open('data.txt', 'r') as f:
    file_lines = f.readlines()

# data = np.array([string.split(' ') for string in file_lines])
data= pd.DataFrame([string.strip('\n').split(' ') for string in file_lines])
print(data.shape)

## PART 1
def check_sorted(report):
    return np.all(report[:-1] <= report[1:]) or np.all(report[:-1] >= report[1:])

def check_difference(report):
    return np.all(np.abs(report[:-1]-report[1:]) >=1 ) and np.all(np.abs(report[:-1]-report[1:]) <=3 )

sum =0
for idx, row in data.iterrows():
    row = np.array(row)
    row = row[row != None]
    row = row.astype(np.int32)
    # print (row)
    
    sum += (check_sorted(row) and check_difference(row))

print (sum)

## PART 2
def check_sorted_asc_ind(report):
    return report[:-1] <= report[1:]

def check_difference_ind(report):
    return np.all(np.abs(report[:-1]-report[1:]) >=1 ) and np.all(np.abs(report[:-1]-report[1:]) <=3)

problem_dampener_list =[]
sum = 0
for idx, row in data.iterrows():
    row = np.array(row)
    row = row[row != None]
    row = row.astype(np.int32)

    if check_sorted(row) and check_difference(row):
        sum +=1
    else:
        for i in range(len(row)): # delete each element and check if it works
            temp = np.delete(row, i)
            if check_sorted(temp) and check_difference(temp):
                sum += 1
                break 



# for idx, report in enumerate(problem_dampener_list):


print (sum)


