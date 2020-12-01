f = open("input.txt", "r")
raw_list = f.readlines()
nums = []
for line in raw_list:
    nums.append(int(line))
nums.sort()
for x in nums:
    y = 2020 - x
    if nums.count(y) > 0:
        print("found: " + str(x) + "," + str(y))
        print("prod: " + str(x * y))
        break
