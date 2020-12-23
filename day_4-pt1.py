# read input
raw_data = open('day4.txt', 'r')

required_fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

data = [x.strip() for x in raw_data.readlines()]
id_data = ''
ids = []

for id in data:
    if id == '':
        ids.append(id_data)
        id_data = ''
        continue
    id_data += id + ' '

current = 0
valid_count = 0

for id in ids:
    id_fields = id.split()
    for field in id_fields:
        key, val = field.split(':')
        if key in required_fields:
            current += 1
    if current == 7:
        valid_count += 1
    current = 0

print("Valid ID Count: " + str(valid_count))
