import math

'''
Rotating to the right:
ex [2, 1] => [-1, 2] => [-2, -1] => [1, -2] => [2, 1]

Rotating to the left:
ex [2, 1] => [1, -2] => [-2, -1] => [-1, 2] => [2, 1]

'''
velocity = [1,10]
coord = [0,0]

dir_map = {"E": (0,1), "W": (0,-1), "N": (1,0), "S": (-1, 0)}
orientation_map = {0 : "E", 90 : "S", 180 : "W", 270 : "N"}

with open("day12.txt", "r") as f:
    for cmd in f:
        cmd_dir = cmd[0]
        cmd_spaces = int(cmd[1:])

        if(cmd_dir == "R"):
            for i in range(cmd_spaces / 90):
                velocity = [velocity[1] * -1, velocity[0]]
        elif(cmd_dir == "L"):
            for i in range(cmd_spaces / 90):
                velocity = [velocity[1], velocity[0] * -1]
        elif(cmd_dir == "F"):
            coord[0] += velocity[0] * cmd_spaces
            coord[1] += velocity[1] * cmd_spaces
        else:
            velocity[0] += dir_map[cmd_dir][0] * cmd_spaces
            velocity[1] += dir_map[cmd_dir][1] * cmd_spaces

        print(coord, velocity, cmd)

print(sum(map(lambda x: abs(x), coord)))
