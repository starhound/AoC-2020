with open('input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split("\n\n")
    input = [line.replace("\n", " ") for line in lines]


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for passport in input:
    if all(x in passport for x in required_fields):
        valid += 1

print("Valid Count: " + str(valid))
