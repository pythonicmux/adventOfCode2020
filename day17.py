lines = []

with open("./day17.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

# [(x,y,z,w) | coordinates for each active cube]
active_cubes = set()

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if(lines[r][c] == '#'):
            active_cubes.add((r, c, 0, 0))

def find_active_neighbors(active_cubes, coord):
    ct = 0
    for x_diff in [-1, 0, 1]:
        for y_diff in [-1, 0, 1]:
            for z_diff in [-1, 0, 1]:
                for w_diff in [-1, 0, 1]:
                    if(x_diff == 0 and y_diff == 0 and z_diff == 0 and w_diff == 0):
                        continue
                    nbr_coord = (coord[0] + x_diff, coord[1] + y_diff, coord[2] + z_diff, coord[3] + w_diff)
                    if(nbr_coord in active_cubes):
                        ct += 1
    return ct

# Simulate one cycle of the conway life game.
def boot_cycle(active_cubes):
    new_active_cubes = set()

    # Check each neighboring cube to an active cube and the
    # active cube itself to see if it changes state. The only
    # cube to change state must be an active cube or a neighbor to
    # an active cube, as new inactive cubes come from active cubes
    # and new inactive cubes must come from a neighbor of a currently
    # active cube, as they are neighbors to exactly 3 active cubes.
    for coord in active_cubes:
        for x_diff in [-1, 0, 1]:
            for y_diff in [-1, 0, 1]:
                for z_diff in [-1, 0, 1]:
                    for w_diff in [-1, 0, 1]:
                        test_coord = (coord[0] + x_diff, coord[1] + y_diff, coord[2] + z_diff, coord[3] + w_diff)
                        num_nbrs = find_active_neighbors(active_cubes, test_coord)

                        # If it's already an active cube it needs 2 or 3 active neighbors to stay active.
                        if (test_coord in active_cubes) and (num_nbrs == 2 or num_nbrs == 3):
                            new_active_cubes.add(test_coord)
                        elif (test_coord not in active_cubes) and (num_nbrs == 3):
                            new_active_cubes.add(test_coord)
    print(len(new_active_cubes))
    return new_active_cubes

for i in range(6):
    active_cubes = boot_cycle(active_cubes)

print(len(active_cubes))
