#goal
goal = 2020

# read input
file = open("input.txt", 'r')

# compile to list
raw_data = file.read().splitlines()
data = []

# convert to ints
for raw_data_point in raw_data:
    data.append(int(raw_data_point))

array_size = len(data)
solutions = []

for i in range(0, array_size - 2):
    for j in range(i + 1, array_size - 1):
        for k in range(j + 1, array_size):
            if data[i] + data[j] + data[k] == goal:
                solutions.append(data[i])
                solutions.append(data[j])
                solutions.append(data[k])

print("First Value: " + str(solutions[0]))
print("Second Value: " + str(solutions[1]))
print("Third Value: " + str(solutions[2]))
print("Total: " + str(solutions[0] * solutions[1] * solutions[2]))
