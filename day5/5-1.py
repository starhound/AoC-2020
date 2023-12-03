def calculate_seat_id(boarding_pass):
    row_range = list(range(128))
    col_range = list(range(8))

    for char in boarding_pass[:7]:
        mid = len(row_range) // 2
        if char == 'F':
            row_range = row_range[:mid]
        elif char == 'B':
            row_range = row_range[mid:]

    for char in boarding_pass[7:]:
        mid = len(col_range) // 2
        if char == 'L':
            col_range = col_range[:mid]
        elif char == 'R':
            col_range = col_range[mid:]

    row = row_range[0]
    col = col_range[0]
    seat_id = row * 8 + col
    return seat_id

def find_highest_seat_id(file_path):
    with open(file_path, 'r') as file:
        boarding_passes = file.read().splitlines()

    highest_seat_id = 0

    for boarding_pass in boarding_passes:
        seat_id = calculate_seat_id(boarding_pass)
        highest_seat_id = max(highest_seat_id, seat_id)

    return highest_seat_id

if __name__ == "__main__":
    file_path = "day5/input.txt"
    result = find_highest_seat_id(file_path)
    print("The highest seat ID is:", result)
