data = open('day6/input.txt', 'r').read().split('\n\n')

total = 0
for line in data:
    print(line)
    print('---')
    total += len(set(line.replace('\n', '')))

print(total)