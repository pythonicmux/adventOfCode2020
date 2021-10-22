lines = []

with open("./day3.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

r_patterns = [1,1,1,1,2]
c_patterns = [1,3,5,7,1]

for i in range(len(r_patterns)):
    r = 0
    c = 0

    ct = 0

    while(r < len(lines)):
        if(lines[r][c] == "#"):
            ct += 1

        if(r == len(lines) - 1):
            break

        c = (c + c_patterns[i]) % len(lines[0])
        r = min(r + r_patterns[i], len(lines) - 1)

    print(ct)

