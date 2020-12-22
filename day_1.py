#goal
goal = 2020

# read input
file = open("input.txt", 'r')

# compile to list
data = file.read().splitlines()

# hold solutions
solutions = []

for num in data:
    first_value = int(num)
    for second in data:
        second_value = int(second)
        total = first_value + second_value
        if total == goal:
            if second_value in solutions:
                break
            solutions.append(first_value)
            solutions.append(second_value)

if len(solutions) == 2:
    print("First Value: " + str(solutions[0]))
    print("Second Value: " + str(solutions[1]))
    print("Total: " + str(solutions[0] * solutions[1]))
    
