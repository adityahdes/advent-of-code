import re
import time
start_time = time.time()
keyval_regex = re.compile(r'([a-z]{3}):(\S+)')


def validate_fields(data):
    if 'byr' not in data:
        return False
    if 'iyr' not in data:
        return False
    if 'eyr' not in data:
        return False
    if 'hgt' not in data:
        return False
    if 'hcl' not in data:
        return False
    if 'ecl' not in data:
        return False
    if 'pid' not in data:
        return False
    return keyref.issuperset(data.keys())


with open('input.txt', 'r') as f:
    passport_data = re.split(r'\n\s*\n', f.read().strip())

keyref = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def part_1():
    count = 0
    for entry in passport_data:
        passport = set([d.split(':')[0] for d in re.split(r'\s+', entry)])
        if passport.issubset(keyref):
            if passport.issuperset(keyref):
                count += 1
            elif passport.symmetric_difference(keyref).issubset(['cid']):
                count += 1
    return count


if __name__ == '__main__':
    print("Day 4, Part 1:", part_1())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))

