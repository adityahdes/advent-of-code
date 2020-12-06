import re
import time
start_time = time.time()
keyval_regex = re.compile(r'([a-z]{3}):(\S+)')
color_regex = re.compile(r'#[0-9a-fA-F]{6}')
pid_regex = re.compile(r'\d{9}')


def extract_passport(data):
    return {k: v for k, v in keyval_regex.findall(data)}


def check_nums(num, min, max):
    return num.isdigit() and int(num) >= min and int(num) <= max


def validate_fields(data):
    if 'byr' not in data or not check_nums(data['byr'], 1920, 2002):
        return False
    if 'iyr' not in data or not check_nums(data['iyr'], 2010, 2020):
        return False
    if 'eyr' not in data or not check_nums(data['eyr'], 2020, 2030):
        return False
    if 'hgt' not in data:
        return False
    elif data['hgt'].endswith('cm'):
        if not check_nums(data['hgt'][:-2], 150, 193):
            return False
    elif data['hgt'].endswith('in'):
        if not check_nums(data['hgt'][:-2], 59, 76):
            return False
    else:  # suffix wrong (neither cm nor in)
        return False
    if 'hcl' not in data or not color_regex.fullmatch(data['hcl']):
        return False
    if 'ecl' not in data or data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if 'pid' not in data or not pid_regex.fullmatch(data['pid']):
        return False
    return keyref.issuperset(data.keys())

with open('input.txt', 'r') as f:
    passport_data = re.split(r'\n\s*\n', f.read().strip())

keyref = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

def part_2():
    passports = [extract_passport(entry) for entry in passport_data]
    count = sum(1 for data in passports if validate_fields(data))
    return count

if __name__ == '__main__':
    print("Day 4, Part 2:", part_2())
    time = (time.time() - start_time)
    print("executed in %s ms or %s ns" % (round(1000 * time), round(1000000000 * time)))

