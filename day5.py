lines = []

with open("./day5.txt", "r") as f:
    for line in f:
        lines.append(line)

seats = [0 for i in range(128 * 8)]

for s in lines:
    r_lo = 0
    r_hi = 127
    c_lo = 0
    c_hi = 7

    for c in s:
        if(c == 'F'):
            r_hi = r_hi - (r_hi - r_lo + 1) / 2
        if(c == 'B'):
            r_lo = r_lo + (r_hi - r_lo + 1) / 2
        if(c == 'L'):
            c_hi = c_hi - (c_hi - c_lo + 1) / 2
        if(c == 'R'):
            c_lo = c_lo + (c_hi - c_lo + 1) / 2

        # print(c, " row:", r_lo, "-", r_hi, " col:", c_lo, "-", c_hi)

    assert(r_lo == r_hi)
    assert(c_lo == c_hi)

    seats[r_lo * 8 + c_lo] = 1

seen1 = False
for i in range(len(seats)):
    if(seen1 and seats[i] == 0):
        print(i)
        break

    if(seats[i] == 1):
        seen1 = True

