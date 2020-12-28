# read input
file = open("day_two_input.txt", 'r')

# compile to list
raw_data = file.read().splitlines()

valid_count = 0

# iterate over all lines
for line in raw_data:
    line_data = line.split()
    # find min/max group from line
    required_value_list = line_data[0].split('-')
    # define required position and banned positions
    required_position = int(required_value_list[0]) - 1
    banned_position = int(required_value_list[1]) - 1
    # determine character in question
    character = line_data[1].split(':')[0]
    # define password
    password = line_data[2]
    split_password = list(password)
    # valid first location
    if split_password[required_position] == character:
        # in first position and second, invalid pwd
        if split_password[banned_position] == character:
            continue
        else:
            valid_count += 1
    else:
        # not in first position, but in second
        if split_password[banned_position] == character:
            valid_count += 1

print("Valid Password Count: " + str(valid_count))
