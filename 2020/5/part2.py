import time

start_time = time.time()

translation = {70: 48, 66: 49, 76: 48, 82: 49}


def part_2():
    with open("input.txt") as f:
        passes = [int(line.strip()[0:7].translate(translation), 2) * 8 + int(line.strip()[7:].translate(translation), 2)
                  for line in f]

    passes.sort()
    seat_id = passes[0]

    for i in range(1, len(passes)):
        if passes[i] != seat_id + 1:
            return int(passes[i]) - 1
        else:
            seat_id = passes[i]


if __name__ == '__main__':
    print("Day 5, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
