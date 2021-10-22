lines = []

with open("./day8.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

def simulate(lines):
    seen_lines = set()
    current_line = 0
    acc = 0

    terminated = True

    while current_line < len(lines):
        instr = lines[current_line]

        if(current_line in seen_lines):
            terminated = False
            break
        else:
            seen_lines.add(current_line)

        if(instr.startswith("acc")):
            acc += int(instr[4 : len(instr)])
        elif(instr.startswith("jmp")):
            current_line += int(instr[4 : len(instr)])
            continue

        current_line += 1

    return terminated, acc

for i in range(len(lines)):
    if lines[i].startswith("nop"):
        lines_copy = [line for line in lines]
        lines_copy[i] = "jmp" + lines[i][3:]

        terminated, acc = simulate(lines_copy)
        if(terminated == True):
            print(acc)
            break
    elif lines[i].startswith("jmp"):
        lines_copy = [line for line in lines]
        lines_copy[i] = "nop" + lines[i][3:]

        terminated, acc = simulate(lines_copy)
        if(terminated == True):
            print(acc)
            break
