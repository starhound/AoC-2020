import re

def is_valid_height(hgt):
    if hgt.endswith("cm"):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith("in"):
        return 59 <= int(hgt[:-2]) <= 76
    return False

def is_valid_hair_color(hcl):
    return bool(re.match(r"^#[0-9a-f]{6}$", hcl))

def is_valid_eye_color(ecl):
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def is_valid_passport_id(pid):
    return bool(re.match(r"^\d{9}$", pid))

def is_valid_passport(passport):
    fields = passport.split()
    for field in fields:
        key, value = field.split(":")
        if key == "byr" and not (1920 <= int(value) <= 2002):
            return False
        elif key == "iyr" and not (2010 <= int(value) <= 2020):
            return False
        elif key == "eyr" and not (2020 <= int(value) <= 2030):
            return False
        elif key == "hgt" and not is_valid_height(value):
            return False
        elif key == "hcl" and not is_valid_hair_color(value):
            return False
        elif key == "ecl" and not is_valid_eye_color(value):
            return False
        elif key == "pid" and not is_valid_passport_id(value):
            return False
    return True

with open('day4/input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split("\n\n")
    input = [line.replace("\n", " ") for line in lines]

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for passport in input:
    if all(x in passport for x in required_fields) and is_valid_passport(passport):
        valid += 1

print("Valid Count: " + str(valid))
