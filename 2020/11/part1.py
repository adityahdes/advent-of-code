import copy
import time


def solve_puzzle(input_arr):
    while True:
        flag = True
        new_board = copy.deepcopy(input_arr)
        for j in range(0, len(input_arr)):
            for i in range(0, len(input_arr[j])):
                neighbours = []
                if i != 0:
                    neighbours.append(input_arr[j][i - 1])
                if i != len(input_arr[j]) - 1:
                    neighbours.append(input_arr[j][i + 1])
                if j != 0:
                    neighbours.append(input_arr[j - 1][i])
                if j != len(input_arr) - 1:
                    neighbours.append(input_arr[j + 1][i])
                if i != 0 and j != 0:
                    neighbours.append(input_arr[j - 1][i - 1])
                if i != len(input_arr[j]) - 1 and j != len(input_arr) - 1:
                    neighbours.append(input_arr[j + 1][i + 1])
                if i != 0 and j != len(input_arr) - 1:
                    neighbours.append(input_arr[j + 1][i - 1])
                if i != len(input_arr[j]) - 1 and j != 0:
                    neighbours.append(input_arr[j - 1][i + 1])
                occupied_neighbours = neighbours.count("#")
                if input_arr[j][i] == "L" and occupied_neighbours == 0:
                    new_board[j][i] = "#"
                    flag = False
                elif input_arr[j][i] == "#" and occupied_neighbours >= 4:
                    new_board[j][i] = "L"
                    flag = False
        if flag:
            sm = 0
            for j in range(0, len(input_arr)):
                for i in range(0, len(input_arr[j])):
                    if input_arr[j][i] == "#":
                        sm += 1
            return sm
        input_arr = new_board


def solve_puzzle2(input_arr):
    num_steps = 0
    while True:
        num_steps += 1
        for line in input_arr:
            print(line)
        print()
        flag = True
        new_board = copy.deepcopy(input_arr)
        for j in range(0, len(input_arr)):
            for i in range(0, len(input_arr[j])):
                neighbours2 = []
                jj = j
                while True:
                    jj += 1
                    if jj >= len(input_arr):
                        break
                    if input_arr[jj][i] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][i])
                        break
                jj = j
                while True:
                    jj -= 1
                    if jj < 0:
                        break
                    if input_arr[jj][i] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][i])
                        break
                ii = i
                while True:
                    ii += 1
                    if ii >= len(input_arr[j]):
                        break
                    if input_arr[j][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[j][ii])
                        break
                ii = i
                while True:
                    ii -= 1
                    if ii < 0:
                        break
                    if input_arr[j][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[j][ii])
                        break
                ii = i
                jj = j
                while True:
                    ii += 1
                    jj += 1
                    if ii >= len(input_arr[j]) or jj >= len(input_arr):
                        break
                    if input_arr[jj][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][ii])
                        break
                ii = i
                jj = j
                while True:
                    ii -= 1
                    jj += 1
                    if ii < 0 or jj >= len(input_arr):
                        break
                    if input_arr[jj][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][ii])
                        break
                ii = i
                jj = j
                while True:
                    ii -= 1
                    jj -= 1
                    if ii < 0 or jj < 0:
                        break
                    if input_arr[jj][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][ii])
                        break
                ii = i
                jj = j
                while True:
                    ii += 1
                    jj -= 1
                    if ii >= len(input_arr[j]) or jj < 0:
                        break
                    if input_arr[jj][ii] in ["#", "L"]:
                        neighbours2.append(input_arr[jj][ii])
                        break
                occupied_neighbours = neighbours2.count("#")
                if input_arr[j][i] == "L" and occupied_neighbours == 0:
                    new_board[j][i] = "#"
                    flag = False
                elif input_arr[j][i] == "#" and occupied_neighbours >= 5:
                    new_board[j][i] = "L"
                    flag = False
        if flag:
            sm = 0
            for j in range(0, len(input_arr)):
                for i in range(0, len(input_arr[j])):
                    if input_arr[j][i] == "#":
                        sm += 1
            return sm
        input_arr = new_board


def part_1():
    input_arr = []
    with open("input.txt") as i_f:
        for line in i_f:
            input_arr.append(list(line.rstrip()))
    return solve_puzzle(input_arr)


if __name__ == '__main__':
    start_time = time.time()
    print("Day 11, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
