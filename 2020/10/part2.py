import time
import re

start_time = time.time()
f = open("input.txt", "r")
nums = [int(i) for i in re.split(r'\n', f.read().strip())]
nums.sort()


def part_2():
    combos = [0] * (nums[-1] + 1)
    combos[0] = 1
    for i in nums:
        combos[i] = combos[i-3] + combos[i-2] + combos[i-1]
    return combos[-1]

if __name__ == '__main__':
    print("Day 10, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))