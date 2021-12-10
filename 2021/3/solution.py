import time
start_time = time.time()
f = open("2021/3/input.txt", "r")
def split(line):
    return list(line)
readings = f.read().splitlines()
vals = []

for reading in readings:
    vals.append(split(reading))

print(vals)

def part_1():

    

# def part_2():
#     position = 0
#     depth = 0
#     aim = 0
#     for cmd, n in instructions:
#         match cmd:
#             case 'down':
#                 aim += n
#             case 'up':
#                 aim -= n
#             case 'forward':
#                 position += n
#                 depth += aim * n
#     return position * depth
        

# if __name__ == '__main__':
#     print("Day 2, Part 1:", part_1())
#     print("Day 2, Part 2:", part_2())
#     time = (time.time() - start_time)
#     print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))