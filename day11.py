lines = []

with open("./day11.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

def find_num_occupied_neighbors(r, c, grid):
    r_directions = [-1, 0, 1]
    c_directions = [-1, 0, 1]

    nbrs = 0

    for dr in r_directions:
        for dc in c_directions:
            nr = r + dr
            nc = c + dc
            while ((dr != 0) or (dc != 0)) and (nr >= 0 and nr < len(grid)) and (nc >= 0 and nc < len(grid[0])):
                if(grid[nr][nc] == "#"):
                    nbrs += 1
                    break
                elif(grid[nr][nc] == "L"):
                    break
                nr = nr + dr
                nc = nc + dc

    return nbrs

def loop_once(grid):
    new_grid = [[x for x in row] for row in grid]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if(grid[r][c] == "."):
                continue

            nbrs = find_num_occupied_neighbors(r, c, grid)
            if(grid[r][c] == "L" and nbrs == 0):
                new_grid[r][c] = "#"
            elif(grid[r][c] == "#" and nbrs >= 5):
                new_grid[r][c] = "L"

    return new_grid

last_grid = [[x for x in row] for row in lines]
grid = loop_once(lines)
iters = 0

while(last_grid != grid):
    last_grid = [[x for x in row] for row in grid]
    grid = loop_once(grid)
    iters += 1

print(grid)

ct = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        ct += (grid[r][c] == "#")

print(ct)

