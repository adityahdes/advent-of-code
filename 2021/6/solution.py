import time
init_time = time.time()
f = open('2021/6/input.txt', 'r')
raw_school = [int(i) for i in f.read().split(',')]
school = [0 for i in range(9)]

for i in raw_school:
    school[i] += 1

def simulate_fish(fish):
    temp = [0 for i in range(9)]
    for i in range(8):
        temp[i] = fish[i+1]
    temp[6] += fish[0]
    temp[8] = fish[0]
    return temp

def run_simulation(num_steps):
    fish = school
    for step in range(num_steps):
        fish = simulate_fish(fish)
    return sum(fish)

if __name__ == '__main__':
    start_time = time.time()
    print("Day 6, Part 1:", run_simulation(80))
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 6, Part 2:", run_simulation(256))
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
    