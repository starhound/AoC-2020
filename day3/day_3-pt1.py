# read input
file = open("input.txt", 'r')

# compile to list
raw_data = file.read().splitlines()

# constants
tree_count = 0
x_position = 0
pattern_width = len(raw_data[0])
tree = '#'

for line in raw_data:
    if line[(x_position % pattern_width)] == tree:
        tree_count += 1
    x_position += 3

print("Tree Count: " + str(tree_count))
