import time
import re

start_time = time.time()
f = open("input.txt", "r")
nums = [int(i) for i in re.split(r'\n', f.read().strip())]


def part_2(data, target):
    for i in range(len(data)):
        range_sum, lo, hi = data[i], data[i], data[i]

        for j in range(i + 1, len(data)):
            current = data[j]
            range_sum, lo, hi = (range_sum + current), (lo if lo < current else current), (hi if hi > current
                                                                                           else current)

            if range_sum > target:
                break
            elif range_sum == target:
                return lo + hi


if __name__ == '__main__':
    print("Day 9, Part 2:", part_2(nums, 23278925))
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
