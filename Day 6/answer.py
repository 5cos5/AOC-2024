from sys import argv

lines: list[str] = []
with open(r'Day 6\data.txt', "r") as f:
    lines = list(line.strip() for line in f.readlines() if line.strip())

sum = 0

grid: list[list[str]] = []

for r, line in enumerate(lines):
    grid.append([])
    grid[-1].append("$")  # Border left
    for c, char in enumerate(line):
        if char == ".":
            grid[-1].append(".")
        elif char == "^":
            loc = (r+1, c+1) # compensate for the border added later
            start = loc
            grid[-1].append("^")
        else:
            grid[-1].append("#") 
    grid[-1].append("$")  # Border right

width = len(grid[0])
blocker = ["$"] * width
grid.insert(0, blocker)  # Border top
grid.append(blocker)  # Border bottom
height = len(grid)

for row in grid:
    print("".join(row))

Coord = tuple[int, int]

Up: Coord = (-1, 0)
Down: Coord = (+1, 0)
Left: Coord = (0, -1)
Right: Coord = (0, +1)

cycle = (Up, Right, Down, Left)

visited: set[Coord] = set()
visited.add(loc)
dir = 0
current = "."

while current != "$":
    # check direction
    visited.add(loc)
    r, c = loc
    dr, dc = cycle[dir]
    next = grid[r+dr][c+dc]
    if next == "#":
        dir = (dir + 1) % 4
        continue
    current = next
    loc = (r+dr, c+dc)

# for r in range(height):
#     for c in range(width):
#         if (r, c) in visited:
#             print("/", end="")
#         else:
#             print(grid[r][c], end="")
#     print()

# PART 1
# print(f"Visited: {len(visited)}")

# PART 2
sum = 0
visited.remove(start)  # Don't hit the guard

print(f"{visited=}")

for obstacle in visited:  # Only one change means that change has to be on the old path somewhere
    loop: set[tuple[Coord, int]] = set()  # loop detection needs location and direction
    loc = start
    dir = 0
    current = "."
    while current != "$":
        # print(f"{loc=}, {dir=}")
        if (loc, dir) in loop:  # we've been here before, looking in the same direction -> loop
            print(f"{loc=}, {dir=}")
            sum += 1
            break
        loop.add((loc, dir))
        r, c = loc
        dr, dc = cycle[dir]
        next = grid[r+dr][c+dc]
        if next == "#" or (r+dr, c+dc) == obstacle:
            dir = (dir + 1) % 4
            continue
        current = next
        loc = (r+dr, c+dc)

print(f"Loops: {sum}")