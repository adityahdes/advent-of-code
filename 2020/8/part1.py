import re
import time
start_time = time.time()
instruction_list = []
f = open("input.txt", "r")
for x in f:
    line = re.match(r'(acc|jmp|nop) (\+\w*|-\w*)', x)
    instruction_list.append((line[1], int(line[2])))


def part_1():
    accumulator = 0
    visited = [False] * len(instruction_list)
    i = 0
    while i in range(0, len(instruction_list)):
        if visited[i]:
            return accumulator
        else:
            visited[i] = True
            instruction = instruction_list[i]
            if instruction[0] == 'nop':
                i += 1
            elif instruction[0] == 'acc':
                accumulator += instruction[1]
                i += 1
            elif instruction[0] == 'jmp':
                i += instruction[1]
            else:
                # this shouldn't happen!
                return -1
    return accumulator


if __name__ == '__main__':
    print("Day 8, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
