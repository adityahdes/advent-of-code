import time
import re

start_time = time.time()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

with open('input.txt', 'r') as f:
    data = re.split(r'\n\s*\n', f.read().strip())


def part_1():
    total_sum = 0
    forms = []
    for d in data:
        forms.append(d.replace("\n", ""))
    for form in forms:
        count = 0
        for alpha in alphabet:
            if form.count(alpha) > 0:
                count += 1
        total_sum += count
    return total_sum


if __name__ == '__main__':
    print("Day 6, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
