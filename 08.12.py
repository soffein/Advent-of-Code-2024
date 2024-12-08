EMPTY = '.'


def load_antenna_locations(grid: list):
    locations = {}
    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if cell is not EMPTY:
                if cell not in locations:
                    locations[cell] = []
                locations[cell].append((row_index, column_index))
    return locations


with open('files/day8input.txt') as file:

    file = [list(line.strip()) for line in file]

antennas = load_antenna_locations(file)
