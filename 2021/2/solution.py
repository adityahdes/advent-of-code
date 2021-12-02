import re
import time
start_time = time.time()
instructions = []
f = open("2021/2/input.txt", "r")
for x in f:
    line = re.match(r'(forward|down|up) (\d)', x)
    instructions.append((line[1], int(line[2])))

def part_1():
    position = 0
    depth = 0
    for cmd, n in instructions:
        match cmd:
            case 'down':
                depth += n
            case 'up':
                depth -= n
            case 'forward':
                position += n
    return position * depth

def part_2():
    position = 0
    depth = 0
    aim = 0
    for cmd, n in instructions:
        match cmd:
            case 'down':
                aim += n
            case 'up':
                aim -= n
            case 'forward':
                position += n
                depth += aim * n
    return position * depth
        

if __name__ == '__main__':
    print("Day 2, Part 1:", part_1())
    print("Day 2, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))