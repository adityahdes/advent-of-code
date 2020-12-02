import re
import time

start_time = time.time()


def check_password(min_val, max_val, letter, password):
    return min_val <= password.count(letter) <= max_val


n = 0
f = open("input.txt", "r")
for x in f:
    r = re.match(r'(.*)-(.*) (.*): (.*)', x)
    if check_password(int(r.group(1)), int(r.group(2)), r.group(3), r.group(4)):
        n += 1
print(n)
print("executed in %s ms" % int(1000 * (time.time() - start_time)))
