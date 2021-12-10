from collections import deque
import time
init_time = time.time()
f = open('2021/10/input.txt', 'r')
lines = f.read().split('\n')

left_delimiters = {'(', '[', '{', '<'}

delimiter_pairs = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}

error_table = {')' : 3,
               ']' : 57,
               '}' : 1197,
               '>' : 25137}

auto_table = {'(' : 1,
              '[' : 2,
              '{' : 3,
              '<' : 4} 

def part_1():
    points = 0
    for line in lines:
        stack = []
        for c in line:
            if c in left_delimiters:
                stack.append(c)
            else:
                if stack[-1] == delimiter_pairs[c]:
                    stack.pop()
                else:
                    points += error_table[c]
                    break
    return points

def part_2():
    scores = []
    incomplete_lines = []
    for line in lines:
        stack = []
        for c in line:
            if c in left_delimiters:
                stack.append(c)
            else:
                if stack[-1] == delimiter_pairs[c]:
                    stack.pop()
                else:
                    stack.clear()
                    break
        remaining = ''
        while len(stack) != 0:
            remaining += stack.pop()
        if len(remaining) != 0:
            incomplete_lines.append(remaining)
    for i in incomplete_lines:
        score = 0
        for j in i:
            score = (5 * score) + auto_table[j]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == '__main__':
    start_time = time.time()
    print("Day 10, Part 1:", part_1())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    start_time = time.time()
    print("Day 10, Part 2:", part_2())
    t = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * t), round(1000000000 * t)))
    tt = (time.time() - init_time)
    print("Total time taken (includes reading input): %s ms or %s ns" % (round(1000 * tt), round(1000000000 * tt)))
