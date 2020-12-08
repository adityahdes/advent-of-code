import collections
import re
import time
start_time = time.time()
contained_in = collections.defaultdict(set)
f = open("input.txt", "r")
for x in f:
    color = re.match(r'(.+?) bags contain', x)[1]
    for ct, inner_color in re.findall(r'(\d+) (.+?) bags?[,.]', x):
        count = int(ct)
        contained_in[inner_color].add(color)

can_hold_gold = set()


def check_color(bag_color):
    for c in contained_in[bag_color]:
        can_hold_gold.add(c)
        check_color(c)


def part_1():
    check_color('shiny gold')
    return len(can_hold_gold)


if __name__ == '__main__':
    print("Day 7, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
