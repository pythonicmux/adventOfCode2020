nums = []

with open("./day9.txt", "r") as f:
    for line in f:
        nums.append(int(line.strip()))

x = 15353384

# Do a prefix sum to get the continguous sum of the numbers in a
# range in constant time.
pref_sum = [0 for i in range(len(nums)+1)]

pref_sum[0] = nums[0]

for i in range(1, len(nums)):
    pref_sum[i] = pref_sum[i-1] + nums[i]

for window_len in range(2, len(nums) + 1):
    for start in range(len(nums) - window_len + 1):
        range_sum = 0
        if(start == 0):
            range_sum = pref_sum[start + window_len - 1]
        else:
            range_sum = pref_sum[start + window_len - 1] - pref_sum[start - 1]

        if(range_sum == x):
            r = [nums[i] for i in range(start, start + window_len)]
            print(min(r), max(r))
            print(min(r) + max(r))
