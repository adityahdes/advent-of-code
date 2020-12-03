import time

start_time = time.time()

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

time = (time.time() - start_time)
print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
