import time
init_time = time.time()
f = open('2021/9/input.txt', 'r')
heights = [[int(i) for i in list(line)] for line in f.read().split('\n')]

def part_1():
    low_points = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            adj = []
            if i-1 >= 0: adj.append(heights[i-1][j])
            if i+1 < len(heights): adj.append(heights[i+1][j])
            if j-1 >= 0: adj.append(heights[i][j-1])
            if j+1 < len(heights[0]): adj.append(heights[i][j+1])
            if(heights[i][j] < min(adj)): low_points.append(heights[i][j])
    return sum(low_points) + len(low_points)



def part_2():
    basin_areas = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            adj = []
            if i-1 >= 0: adj.append(heights[i-1][j])
            if i+1 < len(heights): adj.append(heights[i+1][j])
            if j-1 >= 0: adj.append(heights[i][j-1])
            if j+1 < len(heights[0]): adj.append(heights[i][j+1])
            if(heights[i][j] < min(adj)): 
                basin = [[i, j]]
                for x,y in basin:
                    if x-1 >= 0 and heights[x-1][y] != 9 and [x-1,y] not in basin: basin.append([x-1, y])
                    if x+1 < len(heights) and heights[x+1][y] != 9 and [x+1,y] not in basin: basin.append([x+1, y])
                    if y-1 >= 0 and heights[x][y-1] != 9 and [x,y-1] not in basin: basin.append([x, y-1])
                    if y+1 < len(heights[0]) and heights[x][y+1] != 9 and [x,y+1] not in basin: basin.append([x, y+1])
                basin_areas.append(len(basin))
    basin_areas.sort()
    return basin_areas[-1]*basin_areas[-2]*basin_areas[-3]
                


if __name__ == '__main__':
    start_time = time.time()
    print("Day 9, Part 1:", part_1())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 9, Part 2:", part_2())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
