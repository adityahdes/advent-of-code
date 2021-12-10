from collections import Counter
import time
init_time = time.time()
f = open('2021/5/input.txt', 'r')
segments = [line.replace(' -> ', ',') for line in f.read().split('\n')]

def part_1():
    lines = []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            lines += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
    overlaps = Counter(lines)
    return sum(z > 1 for z in overlaps.values())

def part_2():
    lines = []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            lines += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        elif y1 < y2:
            lines += [(x, y1 + i) for i, x in enumerate(range(x1, x2 + 1))]
        else:
            lines += [(x, y1 - i) for i, x in enumerate(range(x1, x2 + 1))]
    overlaps = Counter(lines)
    return sum(z > 1 for z in overlaps.values())

if __name__ == '__main__':
    start_time = time.time()
    print("Day 5, Part 1:", part_1())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 5, Part 2:", part_2())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
    