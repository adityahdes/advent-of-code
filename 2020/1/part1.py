import time

start_time = time.time()

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

time = (time.time() - start_time)
print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
