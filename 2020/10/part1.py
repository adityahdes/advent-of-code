import time
import re

start_time = time.time()
f = open("input.txt", "r")
nums = [int(i) for i in re.split(r'\n', f.read().strip())]
nums.sort()


def part_1():
    count_1 = 1
    count_3 = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            count_1 += 1
        elif nums[i] - nums[i-1] == 3:
            count_3 += 1
    return count_1 * count_3


if __name__ == '__main__':
    print("Day 10, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))