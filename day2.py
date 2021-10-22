lines = []

with open("./day2.txt", "r") as f:
    for line in f:
        lines.append(line)

valid = 0

for line in lines:
    words = line.split()
    lo, hi = int(words[0].split('-')[0]), int(words[0].split('-')[1])
    letter = words[1][0]
    word = words[2]

    cond1 = (word[lo-1] != letter and word[hi-1] == letter)
    cond2 = (word[lo-1] == letter and word[hi-1] != letter)
    if(cond1 or cond2):
        valid += 1

print(valid)
