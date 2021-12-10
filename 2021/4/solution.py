import time
start_time = time.time()
f = open('2021/4/input.txt', 'r')

num_data, *board_data = f.read().split('\n\n')

def init_boards(num_data, board_data):
    nums = map(int, num_data.split(','))
    boards = []
    for board in board_data:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return nums, boards

def calc_score(n, board):
    return (sum(sum(group) for group in board) - n) * n

def part_1():
    nums, boards = init_boards(num_data, board_data)
    for n in nums:
        for i, board in enumerate(boards):
            if {n} in board:
                return calc_score(n, board)
            else:
                boards[i] = [group.difference({n}) for group in board]

def part_2():
    nums, boards = init_boards(num_data, board_data)
    for n in nums:
        for i, board in enumerate(boards):
            if board is not None:
                if {n} in board:
                    winner = calc_score(n, board)
                    boards[i] = None
                    if i % 2:
                        boards[i-1] = None
                    else:
                        boards[i+1] = None
                else:
                    boards[i] = [group.difference({n}) for group in board]
    return winner

if __name__ == '__main__':
    print("Day 4, Part 1:", part_1())
    print("Day 4, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))