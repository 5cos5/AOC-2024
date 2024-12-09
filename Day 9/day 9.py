import timeit

start = timeit.default_timer()
with open(r'Day 9\data.txt', 'r') as f:
    file = f.readlines()

line = file[0]

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
print (disk)
print(len(disk))
def compact_disk(disk):
    uncompacted = True
    disk_length = len(disk)
    # temp_disk = disk
    while uncompacted:
        try:
            dot_index = disk.index('.')
        except:
            uncompacted = False
            continue
        # num_index = len(temp_disk)-1
        num = disk.pop()
        if str(num).isdigit():
            disk[dot_index] = num
        else:
            continue
    return disk
compacted_disk = compact_disk(disk)
print (compacted_disk)
print (len(compacted_disk))

def checksum(disk):
    sum=0
    for idx, num in enumerate(disk):
        sum += num*idx
        # print (num, idx)
        # print (sum)
    return sum

print (checksum(compacted_disk))
print("The difference of time is :",
              timeit.default_timer() - start)