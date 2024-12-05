import copy
with open(r'Day 5\data_rules.txt', 'r') as f:
    file_lines = f.readlines()

rules = []
rules_1 = []
rules_2 =[]
for idx, line in enumerate(file_lines):
    line =line.replace("\n", "")
    split = (tuple(line.split('|')))
    rules.append(split)
    rules_1.append(split[0])
    rules_2.append(split[1])


with open(r'Day 5\data_update.txt', 'r') as f:
    file_lines = f.readlines()
# Part 1
incorrect_lines =[]
correct_lines = []
for line in file_lines:
    CORRECT = True
    line = line.replace("\n", "").split(',')
    for idx, num in enumerate(line):
        num_after = line[idx+1:]
        for number in num_after:
            indices = [i for i, x in enumerate(rules_2) if x == number]
            rules_before_pages = [rules_1[i] for i in indices] ## find all pages that should exist b4 the num_after
            if num not in rules_before_pages:
                CORRECT = False
    if CORRECT:
        correct_lines.append(line)
    else:
        incorrect_lines.append(line)
print (len(correct_lines))
print (len(incorrect_lines))
print (len(file_lines))
sum =0
for line in correct_lines:
    num = line[int(len(line)/2)]
    sum += int(num)

print (sum)

# Part 2
to_fix =True
while to_fix:
    corrected_lines = []
    broken_rules = []
    for line in incorrect_lines:
        new_line = copy.deepcopy(line)
        
        for idx, num in enumerate(line):
            num_after = line[idx+1:]
            for number in num_after:
                indices = [i for i, x in enumerate(rules_1) if x == number]
                rules_after_pages = [rules_2[i] for i in indices]
                if num in rules_after_pages:
                    a, b = line.index(number), line.index(num)
                    line[b], line[a] = line[a], line[b]
                    broken_rules.append((number,num))
        corrected_lines.append(line)
    incorrect_lines = corrected_lines
    if len(broken_rules) ==0:
        to_fix =False


print(corrected_lines)
sum =0
for line in corrected_lines:
    num = line[int(len(line)/2)]
    sum += int(num)

print (sum)