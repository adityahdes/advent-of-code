import time
init_time = time.time()
f = open('2021/8/input.txt', 'r')
signals = [[set(i) for i in line.split()] for line in f.read().split('\n')]

def part_1():
    out = 0
    for signal in signals:
        out += sum(len(digit) in (2, 3, 4, 7) for digit in signal[-4:])
    return out

def part_2():
    out = 0
    for signal in signals:
        patterns = sorted(signal[:10], key=len)
        patterns[3:6] = sorted(patterns[3:6], key=lambda x: (patterns[1].issubset(x), len(patterns[2] & x)))
        patterns[6:9] = sorted(patterns[6:9], key=lambda x: (patterns[2].issubset(x), patterns[1].issubset(x)))
        patterns = [patterns[i] for i in (7, 0, 3, 5, 2, 4, 6, 1, 9, 8)]
        result = ''
        for digit in signal[-4:]:
            for i, pattern in enumerate(patterns):
                if pattern == digit:
                    result += str(i)
        out += int(result)
    return out

if __name__ == '__main__':
    start_time = time.time()
    print("Day 8, Part 1:", part_1())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 8, Part 2:", part_2())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
    