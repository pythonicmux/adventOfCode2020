lines = []

with open("./day4.txt", "r") as f:
    lines.append([])
    for line in f:
        if(len(line) <= 1):
            lines.append([])
        else:
            lines[len(lines)-1].extend(line.strip().split())

ct = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_ecl = set("amb blu brn gry grn hzl oth".split())
for line in lines:
    passport = {}
    for word in line:
        key,value = word.split(':')[0], word.split(':')[1]
        passport[key] = value

    valid = True
    for k in keys:
        if(k not in passport):
            valid = False
        else:
            v = passport[k]
            if(k == "byr"):
                valid &= passport[k].isdigit() and int(passport[k]) >= 1920 and int(passport[k]) <= 2002
            if(k == "iyr"):
                valid &= passport[k].isdigit() and int(passport[k]) >= 2010 and int(passport[k]) <= 2020
            if(k == "eyr"):
                valid &= passport[k].isdigit() and int(passport[k]) >= 2020 and int(passport[k]) <= 2030
            if(k == "hgt"):
                valid &= (len(v) == 4 and (v[2:] == "in") and (v[:2].isdigit()) and int(v[:2]) >= 59 and int(v[:2]) <= 76) or \
                        (len(v) == 5 and (v[3:] == "cm") and (v[:3].isdigit()) and int(v[:3]) >= 150 and int(v[:3]) <= 193)
            if(k == "hcl"):
                valid &= v[0] == "#" and len(v) == 7
                if(valid):
                    for i in range(1,7):
                        valid &= (v[i].isalpha() and (ord(v[i]) - ord("a") >= 0) and (ord(v[i]) - ord("a") <= 5)) or \
                                (v[i].isdigit and int(v[i]) >= 0 and int(v[i]) <= 9)
            if(k == "ecl"):
                valid &= (v in valid_ecl)

            if(k == "pid"):
                valid &= (v.isdigit() and len(v) == 9)

    for k in passport:
        if(k not in keys and k != "cid"):
            valid = False

    if(valid):
        ct += 1

print(ct)


