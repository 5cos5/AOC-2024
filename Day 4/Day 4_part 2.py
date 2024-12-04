with open(r'Day 4\data.txt', 'r') as f:
    file_lines = f.readlines()

data = [[0]]*len(file_lines)
for idx, line in enumerate(file_lines):
    data[idx] = line.replace("\n", "")

def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1
 
# Function that returns all adjacent elements
def getAdjacent(arr, i, j):
 
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    # Initialising a vector array
    # where adjacent element will be stored
    v = {}
 
    # Checking for all the possible adjacent positions
    if (isValidPos(i - 1, j - 1, n, m)):
        v['topleft']=(arr[i - 1][j - 1])
    
    if (isValidPos(i - 1, j + 1, n, m)):
        v['topright']=(arr[i - 1][j + 1])
    
    if (isValidPos(i + 1, j - 1, n, m)):
        v['bottomleft']=(arr[i + 1][j - 1])
    
    if (isValidPos(i + 1, j + 1, n, m)):
        v['bottomright']= (arr[i + 1][j + 1])
 
    # Returning the vector
    return v
pairs = {
    'bottomleft': 'topright',
    # 'topright': 'bottomleft',
    'bottomright':'topleft',
    # 'topleft':'bottomright'
}
# data = data[5:]
total = 0
for row, line in enumerate(data):
    for col, letter in enumerate(line):
        if letter == 'A':
            temp = 0
            adj = getAdjacent(data,row,col)
            print (row,col)
            print (adj)
            for k,v in adj.items():
                dir1 = k
                if dir1 in pairs.keys():
                    next_dir = pairs[dir1]
                    if next_dir in adj.keys():
                        if v == 'M' and adj[next_dir] == 'S':
                            temp += 1
                        elif v == 'S' and adj[next_dir] == 'M':
                            temp +=1
            if temp ==2:
                total +=1
            



print ("Total",total)


 