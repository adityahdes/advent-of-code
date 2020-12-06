import time
import re

start_time = time.time()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

with open('input.txt', 'r') as f:
    data = re.split(r'\n\s*\n', f.read().strip())


def part_2():
    total_sum = 0
    groups = []
    for d in data:
        groups.append(d.split("\n"))
    for group in groups:
        s = len(group)
        group_count = 0
        for alpha in alphabet:
            count = 0
            for form in group:
                if form.count(alpha) == 1:
                    count += 1
            if count == s:
                group_count += 1
        total_sum += group_count
    return total_sum


if __name__ == '__main__':
    print("Day 6, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
