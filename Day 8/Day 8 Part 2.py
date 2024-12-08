import itertools
import numpy as np
with open(r'Day 8\data.txt', 'r') as f:
    file = f.readlines()
grid = []
# antinode = []
for line in file:
    line = line.rstrip('\n')
    temp_line = [i for i in line]
    temp_antinode = [0 for i in line]
    grid.append(temp_line)
    # antinode.append(temp_antinode)
y_len = len(grid)
x_len = len(grid[0])

def find_freq_pos(grid):
    freq_dict= {}
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos == '.':
                continue
            elif  pos not in freq_dict.keys():
                freq_dict[pos] = [(y,x)]
            else:
                freq_dict[pos].append((y,x))
    return freq_dict

freq_dict = find_freq_pos(grid)

def isBetween(a, b, c, epsilon = 0.01):
    crossproduct = (c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > epsilon:
        return False
    return True
antinodes = []
for k in freq_dict.keys():
    points = freq_dict[k]
    point_pairs = list(itertools.combinations(points,2))
    for point_pair in point_pairs:
        n = 1
        end_reached = False
        for n in range(max(x_len,y_len)):
            # print (n)
            # print ("Point_piar", point_pair)
            point1 = point_pair[0]
            point2 = point_pair[1]
            antinode_y1,antinode_x1 = point1[0]+ n*(point1[0]-point2[0]), point1[1]+n*(point1[1]-point2[1])
            antinode_y2,antinode_x2 = point1[0]+ n*(point1[0]+point2[0]), point1[1]+n*(point1[1]-point2[1])
            antinode_y3,antinode_x3 = point1[0]+ n*(point1[0]-point2[0]), point1[1]+n*(point1[1]+point2[1])
            antinode_y4,antinode_x4 = point1[0]+ n*(point1[0]+point2[0]), point1[1]+n*(point1[1]+point2[1])
            antinode_y5,antinode_x5 = point2[0]+ n*(point2[0]-point1[0]), point2[1]+n*(point2[1]-point1[1])
            antinode_y6,antinode_x6 = point2[0]+ n*(point2[0]+point1[0]), point2[1]+n*(point2[1]-point1[1])
            antinode_y7,antinode_x7 = point2[0]+ n*(point2[0]-point1[0]), point2[1]+n*(point2[1]+point1[1])
            antinode_y8,antinode_x8 = point2[0]+ n*(point2[0]+point1[0]), point2[1]+n*(point2[1]+point1[1])
            temp_antinodes = [(antinode_y1,antinode_x1),(antinode_y2,antinode_x2),(antinode_y3,antinode_x3),(antinode_y4,antinode_x4),
                            (antinode_y5,antinode_x5),(antinode_y6,antinode_x6),(antinode_y6,antinode_x6),(antinode_y6,antinode_x6)]
            for antinode in temp_antinodes:
                x = antinode[1]
                y = antinode[0]
                if (0 <= y < y_len):
                    if (0 <= x < x_len):
                        if isBetween(point1,point2,antinode):
                            print (antinode)
                            antinodes.append(antinode)

print (len(set(antinodes)))
