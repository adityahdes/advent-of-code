import time

# start timer
start_time = time.time()

# import data
f = open("2021/1/input.txt", "r")
raw_list = f.readlines()
nums = []
for line in raw_list:
        nums.append(int(line))

def part_1(nums):
    count = 0
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1]:
            count += 1
    return count

def part_2(nums):
    count = 0
    for i in range(len(nums)-3):
        if nums[i+3] > nums[i]:
            count += 1
    return count

print("Part 1:", part_1(nums))
print("Part 2:", part_2(nums))
time = (time.time() - start_time)
print("executed in %s ms or %s ns" %
      (round(1000 * time), round(1000000000 * time)))
