def sum_of_counts(file_path):
    with open(file_path, 'r') as file:
        groups = file.read().strip().split('\n\n')

    total_sum = 0

    for group in groups:
        # Split each group into individual answers
        answers = [set(person) for person in group.split('\n')]

        # If the group is empty, skip to the next one
        if not answers[-1]:
            continue

        # Use set intersection to find common "yes" answers in the group
        common_yes = set.intersection(*answers)

        # Increment the total sum by the count of common "yes" answers
        total_sum += len(common_yes)

    return total_sum

if __name__ == "__main__":
    file_path = "day6/input.txt"
    result = sum_of_counts(file_path)
    print("The sum of counts where everyone answered 'yes' is:", result)
