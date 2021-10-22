nums = [12,1,16,3,11,0]

last_spoken = {}
turn = 1

for n in nums:
    last_spoken[n] = turn
    turn += 1

last_number = nums[-1]
number = 0

while(turn <= 30000000):
    # print("Turn:", turn, "Last number:", last_number)
    # print(last_spoken)
    if (last_number not in last_spoken) or (last_spoken[last_number] == turn-1):
        number = 0
    else:
        number = turn - 1 - last_spoken[last_number]
    last_spoken[last_number] = turn-1
    last_number = number
    turn += 1

print(last_number)
