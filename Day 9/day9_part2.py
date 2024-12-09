from tqdm import tqdm
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
with open(r'data.txt', 'r') as f:
    file = f.readlines()

line = file[0]
def generate_disk_map(line):
    grid = []
    empty_space = []
    for idx, num in enumerate(line):
        if idx %2 == 0: # file block
            grid.append(int(num))
        elif idx %2 ==1: #empty block
            empty_space.append(int(num))
    grid = grid[::-1]
    return grid

def generate_disk(line):
    disk = []
    count = 0
    for idx, num in enumerate(line):
        if idx %2 == 0: # file block
            # print (num)
            for x in range(int(num)):
                # print(num)
                disk.append(count)
            count+=1
        elif idx %2 ==1:
            for x in range(int(num)):
                disk.append('.')
    return disk
disk = generate_disk(line)
# print ("Original disk",disk)
# print(len(disk))
def find_empty_space(disk):
    count = 0
    empty_space_dict = {}
    for num_idx, num in enumerate(disk):
        if num == '.':
            count += 1
        elif num != '.' and count !=0:
            if count not in empty_space_dict.values(): #only save values which are unique to optimise
                empty_space_dict[num_idx-count] = count 
            count = 0
        if len(empty_space_dict.keys()) == 9: #found all possible lengths,added to optimise
            return empty_space_dict
    return empty_space_dict

def compact_disk(disk):
    uncompacted = True
    disk_length = len(disk)
    temp_disk = [i for i in disk if i != '.']
    max_num = max(temp_disk)
    max_num_range = [i for i in range(max_num+1)][::-1]
    grid = generate_disk_map(line)
    # print (grid)
    for idx, num in enumerate(tqdm(max_num_range)):
        num_length = grid[idx]
        empty_spaces = find_empty_space(disk[:disk.index(num)+1]) #added this to optimise
        for k,v in empty_spaces.items():
            if v>= num_length:# and disk.index(num) > k:
                # print (num, num_length)
                disk = [i if i != num else '.' for i in disk ]
                # print ("removed",disk)
                disk[k:k+num_length] = [num for i in range(num_length)]
                # print (disk)
                break
    return disk
compacted_disk = compact_disk(disk)
# print (compacted_disk)

# print (len(compacted_disk))

def checksum(disk):
    sum=0
    for idx, num in enumerate(disk):
        if str(num).isdigit():
            sum += num*idx
            # print (num, idx)
            # print (sum)
    return sum

print (checksum(compacted_disk)) 
## First run takes 5 mins to solve...
## Second optimised run takes 1.30 to solve...
## Third optimised run takes 1.05 to solve...

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())