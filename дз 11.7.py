nums = []

f = open("numbers.txt", "r")
for line in f:
    nums.append(int(line))
f.close()

nums.sort()
print(nums)