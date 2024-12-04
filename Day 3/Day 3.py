import numpy as np
from copy import deepcopy
with open('data.txt', 'r') as f:
    file_lines = f.readlines()


lines =[]

def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]
for line in file_lines:
    lines.append(line.split('mul('))
lines = flatten_comprehension(lines)

## PART 1
num1_list = []
num2_list = []
for line in lines:
    # print (line)
    sub_lines = line.split(',')
    # print (len(sub_lines))
    if len(sub_lines) <2:
        continue
    digit1 = sub_lines[0]
    digit1_bool = None
    if digit1.isdigit():
        digit1_bool = True
    sub_sub_lines = sub_lines[1].split(')')
    digit2 = sub_sub_lines[0]
    digit2_bool = None
    if digit2.isdigit():
        digit2_bool =True
    if digit1_bool and digit2_bool:
        num1_list.append(int(digit1))
        num2_list.append(int(digit2))

# print (num1_list)
print (sum(np.array(num1_list)*np.array(num2_list)))

## PART 2
num1_list = []
num2_list = []
def check(data):
    for d in data[::-1]: #check backwards as only most recent one matters
        if "don't()" in d:
            # print("FALSE")
            return False
        if "do()" in d:
            return True

ENABLED = True
test =[]
for line in lines:
    sub_lines = line.split(',')
    if len(sub_lines) <2: ### THIS WAS THE bug. NEED TO CHECK ENABLED STATUS EVEN IF NO MUL
        if check(sub_lines) == None:
            continue
        else:
            ENABLED = check(sub_lines)
            continue
    digit1 = sub_lines[0]
    digit1_bool = None
    if digit1.isdigit():
        digit1_bool = True
    sub_sub_lines = sub_lines[1].split(')')
    digit2 = sub_sub_lines[0]
    digit2_bool = None
    if digit2.isdigit():
        digit2_bool =True
    if digit1_bool and digit2_bool and ENABLED:
        num1_list.append(int(digit1))
        num2_list.append(int(digit2))
        test.append([int(digit1),int(digit2)])

    if check(sub_lines) == None:
        continue
    else:
        ENABLED = check(sub_lines)
    
print (sum(np.array(num1_list)*np.array(num2_list)))
# print (num1_list)
