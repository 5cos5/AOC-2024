with open(r'Day 6\test.txt', 'r') as f:
    file = f.readlines()
grid = []
for line in file:
    line = line.rstrip('\n')
    temp_line = [i for i in line]
    grid.append(temp_line)

## Part 1
def find_start(grid):
    direction = None
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos == '^':
                direction = 'up'
                return (y,x), direction
            if pos == '>':
                direction = 'right'
                return (y,x), direction
            if pos == '<':
                direction = 'left'
                return (y,x), direction
            if pos == 'v':
                direction = 'down'
                return (y,x), direction

def isValidPos(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def move(grid,position,direction):
    change_pos_dict = {'up': (-1,0),
                      'right': (0,1),
                      'left':(0,-1),
                      'down':(1,0)}
    change_dir_dict = {'up': 'right',
                      'right': 'down',
                      'left': 'up',
                      'down': 'left'}
    change = change_pos_dict[direction]
    new_y = position[0]+change[0]
    new_x = position[1]+change[1]
    y_lim = len(grid)
    x_lim = len(grid[0])
    if isValidPos(new_y,new_x,y_lim,x_lim):
        if grid[new_y][new_x] == '.':
            return (new_y,new_x) , direction
        elif grid[new_y][new_x] == '#':
            direction = change_dir_dict[direction]
            return position , direction
    else:
        # direction = change_dir_dict[direction]
        direction = False
        return position, direction


postion , direction = find_start(grid)
start_pos, start_dir = postion,direction
grid[postion[0]][postion[1]] = '.'
postion_moved = [postion]
while direction:
    postion , direction = move(grid, postion,direction)
    postion_moved.append(postion)


unique_pos = set(postion_moved)

print(len(unique_pos))
## Part 2
def check_cycling(grid,postion,direction):
    postion_moved = [postion]
    position_dict ={}
    position_dict[postion] = [direction]
    cycling = False
    while direction:
        postion , direction = move(grid, postion,direction)
        postion_moved.append(postion)
        if postion not in position_dict.keys():
            position_dict[postion] = [direction]
        else:
            if direction in position_dict[postion]:
                direction = False
                cycling =True
            else:
                position_dict[postion].append(direction)
                # print((postion,direction))
    return cycling
# grid[6][3] = '#'
for j, line in enumerate(grid):
    for i, pos in enumerate(line):
        if j == start_pos[0] and i == start_pos[1]:
            continue
        else:
            grid[j][i] = '#'
            cycling = check_cycling(grid,postion,direction)