lines = []

with open("./day6.txt", "r") as f:
    lines.append([])
    for line in f:
        if(len(line) <= 1):
            lines.append([])
        else:
            lines[len(lines)-1].extend(line.strip().split())

ct = 0
for line in lines:
    qs = {}
    for word in line:
        for c in word:
            if c not in qs:
                qs[c] = 0
            qs[c] += 1

    for k in qs:
        if(qs[k] == len(line)):
            ct += 1

print(ct)

