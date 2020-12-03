import time

start_time = time.time()
with open(f'input.txt') as f:
    ski_course = [line.strip() for line in f]


def part_2(course, trajectories):
    product = 1
    for trajectory in trajectories:
        product *= count_trees(course, trajectory[0], trajectory[1])
    return product


def count_trees(course, right, down):
    count = 0
    for i, ski in enumerate(course[::down]):
        if ski[i * right % len(ski)] == '#':
            count += 1
    return count


if __name__ == '__main__':
    print("Day 3, Part 2:", part_2(ski_course, {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}))
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
