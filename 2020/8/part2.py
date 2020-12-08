import re
import time
start_time = time.time()
instruction_list = []
f = open("input.txt", "r")
for x in f:
    line = re.match(r'(acc|jmp|nop) (\+\w*|-\w*)', x)
    instruction_list.append((line[1], int(line[2])))


def read_instructions(lst):
    accumulator = 0
    visited = [False] * len(lst)
    i = 0
    while i in range(0, len(lst)):
        if visited[i]:
            return False, accumulator
        else:
            visited[i] = True
            instruction = lst[i]
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
    return True, accumulator


def part_2():
    for i in range(0, len(instruction_list)):
        if instruction_list[i][0] == 'acc':
            continue
        elif instruction_list[i][0] == 'jmp':
            new_instructions = instruction_list.copy()
            new_instructions[i] = ('nop', instruction_list[i][1])
            result = read_instructions(new_instructions)
            if result[0]:
                print("Changed instruction at index %d from jmp to nop" % i)
                return result[1]
        elif instruction_list[i][0] == 'nop':
            new_instructions = instruction_list.copy()
            new_instructions[i] = ('jmp', instruction_list[i][1])
            result = read_instructions(new_instructions)
            if result[0]:
                print("Changed instruction at index %d from nop to jmp" % i)
                return result[1]
        else:
            # this shouldn't happen either!
            continue
    return -1


if __name__ == '__main__':
    print("Day 8, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
