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
    print(part_2(ski_course, {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}))
