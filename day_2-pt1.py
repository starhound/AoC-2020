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
    # define min/max
    min = int(required_value_list[0])
    max = int(required_value_list[1])
    # determine character in question
    character = line_data[1].split(':')[0]
    # define password
    password = line_data[2]
    # count required character in password
    password_character_count = password.count(character)
    # if character greater than or equal to min character count
    if password_character_count >= min:
        # and if character count less than or equal to max
        if password_character_count <= max:
            # valid pwd
            valid_count += 1

print("Valid Password Count: " + str(valid_count))
