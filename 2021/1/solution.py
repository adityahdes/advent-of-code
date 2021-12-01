import time

start_time = time.time()

f = open("input.txt", "r")
raw_list = f.readlines()
nums = []
count = 0
for line in raw_list:
    nums.append(int(line))

for i in range(1, len(nums)-1):
    if nums[i] > nums[i-1]:
        count += 1

print(count)

count = 0
start_time = time.time()

for i in range(len(nums)-3):
    if sum(nums[i+1:i+4]) > sum(nums[i:i+3]):
        count += 1



print(count)

time = (time.time() - start_time)
print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))