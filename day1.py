nums = []

with open("./day1.txt", "r") as f:
    for line in f:
        nums.append(int(line))

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if (i != j) and (i != k) and (nums[i] + nums[j] + nums[k] == 2020):
                print(nums[i], nums[j], nums[k])
                print(nums[i]*nums[j]*nums[k])
