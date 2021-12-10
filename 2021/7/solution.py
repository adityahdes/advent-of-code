import time
init_time = time.time()
f = open('2021/7/input.txt', 'r')
vals = [int(i) for i in f.read().split(',')]

def cost(a, b):
    c = abs(a - b)
    return (c * (c + 1))//2

def part_1():
    lo, hi = min(vals), max(vals) + 1
    costs = []
    for i in range(lo, hi):
        costs.append(sum(abs(j - i) for j in vals))
    return min(costs)

def part_2():
    lo, hi = min(vals), max(vals) + 1
    costs = []
    for i in range(lo, hi):
        costs.append(sum(cost(i, j) for j in vals))
    return min(costs)

if __name__ == '__main__':
    start_time = time.time()
    print("Day 7, Part 1:", part_1())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 7, Part 2:", part_2())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
    