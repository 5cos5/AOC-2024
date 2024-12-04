with open(r'Day 4\data.txt', 'r') as f:
    file_lines = f.readlines()

data = [[0]]*len(file_lines)
for idx, line in enumerate(file_lines):
    data[idx] = line.replace("\n", "")

def direction_points(g_len_x, g_len_y, point_x, point_y,data):
    result = {}

    directions = {
        'up':[0, -1],  
        'upright':[1, -1], 
        'right':[1, 0],    
        'downright':[1, 1],  
        'down':[0, 1],    
        'downleft':[-1, 1],   
        'left':[-1, 0], 
        'leftup':[-1, -1]
        }

    for key,direction in directions.items():

        x = point_x
        y = point_y
        end_reached = False
        while not end_reached:

            x = x + direction[0]
            y = y + direction[1]
            count = 0
            if (0 <= y < g_len_y) and not end_reached:
                if (0 <= x < g_len_x) and not end_reached:
                    if key not in result.keys():
                        result[key] = (data[y][x])
                        count += 1
                    else:
                        result[key] += (data[y][x])
                        count +=1
                else:
                    end_reached = True
            else:
                end_reached = True

    return result

# data = data[4:]
total = 0
for row, line in enumerate(data):
    for col, letter in enumerate(line):
        if letter == 'X':
            letters = direction_points(len(data[0]),len(data),col,row,data)
            for value in letters.values():
                if value.startswith('MAS'):
                    total +=1

print (total)
'''
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
    if (isValidPos(i - 1, j, n, m)):
        v['top']=(arr[i - 1][j])
    if (isValidPos(i - 1, j + 1, n, m)):
        v['topright']=(arr[i - 1][j + 1])
    if (isValidPos(i, j - 1, n, m)):
        v['left']=(arr[i][j - 1])
    if (isValidPos(i, j + 1, n, m)):
        v['right']=(arr[i][j + 1])
    if (isValidPos(i + 1, j - 1, n, m)):
        v['bottomleft']=(arr[i + 1][j - 1])
    if (isValidPos(i + 1, j, n, m)):
        v['bottom'] = (arr[i + 1][j])
    if (isValidPos(i + 1, j + 1, n, m)):
        v['bottomright']= (arr[i + 1][j + 1])
 
    # Returning the vector
    return v

def check_direction(data,row,col,direction):
    direction_dict = {
        'topleft' = [[row-2][col-2], [row-3][col-3], [row-4][col-4]]
    }


def find_MAS(data,row,col):
    direction = None
    adj = getAdjacent(data,row,col)
    for k,v in adj.items():
        if v =='M':
            direction = k


    if direction == None:
        return False
    else:
        return True

    '''