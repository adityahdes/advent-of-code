import collections
import re
import time
start_time = time.time()
contains = collections.defaultdict(list)
f = open("input.txt", "r")
for x in f:
    color = re.match(r'(.+?) bags contain', x)[1]
    for ct, inner_color in re.findall(r'(\d+) (.+?) bags?[,.]', x):
        count = int(ct)
        contains[color].append((count, inner_color))


def bag_cost(bag_color):
    total = 0
    for ct, inner_color in contains[bag_color]:
        total += ct
        total += ct * bag_cost(inner_color)
    return total

if __name__ == '__main__':
    print("Day 7, Part 2:", bag_cost('shiny gold'))
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
