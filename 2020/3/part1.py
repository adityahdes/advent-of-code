import time

start_time = time.time()

with open(f'input.txt') as f:
    ski_course = [line.strip() for line in f]


def part_1(course):
    count = 0
    for i, ski in enumerate(course):
        if ski[i * 3 % len(ski)] == '#':
            count += 1
    return count


if __name__ == '__main__':
    print("Day 3, Part 1:", part_1(ski_course))
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
