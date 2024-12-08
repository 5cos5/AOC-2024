import itertools
from tqdm import tqdm
with open(r'Day 7\data.txt', 'r') as f:
    file = f.readlines()

ans = []
eqns = []
for line in file:
    line = line.rstrip('\n')
    line = line.split(':')
    ans.append(line[0])
    eqn = line[1].lstrip(' ').split(" ")
    eqn = list(map(int, eqn))
    eqns.append(eqn)

def run_operations(eqn,operators):
    sum = eqn[0]
    for idx, num in enumerate(eqn[1:]):
        if operators[idx] == 1: #plus
            sum += num
        elif operators[idx] == 2: #multiply
            sum *= num
        elif operators[idx] ==3: #concat
            sum = int(str(sum) + str(num))
    return sum
operators = [1,2,3]
total = 0
for eqn_idx, eqn in enumerate(tqdm(eqns)):
    # print (eqn)
    if len(eqn)-1 ==1:
        to_test = [[1],[2],[3]]
    else:
        to_test = [p for p in itertools.product(operators, repeat=len(eqn)-1)]
    # print (to_test)
    for permutation in tqdm(to_test,leave=False):
        # print (permutation)
        temp_ans = run_operations(eqn,permutation)
        # print (temp_ans)
        # print ("ans",ans[eqn_idx])
        if int(temp_ans) == int(ans[eqn_idx]):
            # print("Passed ",temp_ans)
            total += temp_ans
            break

print (total)

