f = open("input.txt", "r")
raw_list = f.readlines()
nums = []
for line in raw_list:
    nums.append(int(line))
nums.sort()


def find_2(i, nums, sum):
    nums.sort()
    for x in nums:
        y = sum - x
        if nums.count(y) > 0:
            print("found: " + str(i) + "," + str(x) + "," + str(y))
            print("prod: " + str(i * x * y))
            return True


for x in nums:
    y = 2020 - x
    if find_2(x, nums, y):
        break
