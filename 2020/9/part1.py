import time
import re

start_time = time.time()
f = open("input.txt", "r")
nums = [int(i) for i in re.split(r'\n', f.read().strip())]


def check_valid(preamble, num):
    for i in preamble:
        if (num - i) in preamble:
            return True
    return False


def part_1():
    for i in range(25, len(nums)):
        if not check_valid(nums[i - 25: i], nums[i]):
            return nums[i]
    return -1


if __name__ == '__main__':
    print("Day 9, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
