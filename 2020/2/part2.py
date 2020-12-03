import re
import time

start_time = time.time()


def check_password(pos_1, pos_2, letter, password):
    char_1 = password[pos_1 - 1]
    char_2 = password[pos_2 - 1]
    if char_1 == char_2:
        return False
    return char_1 == letter or char_2 == letter


n = 0
f = open("input.txt", "r")
for x in f:
    r = re.match(r'(.*)-(.*) (.*): (.*)', x)
    if check_password(int(r.group(1)), int(r.group(2)), r.group(3), r.group(4)):
        n += 1

print("Day 2, Part 2:", n)
time = (time.time() - start_time)
print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))
