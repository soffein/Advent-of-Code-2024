from itertools import product

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


def calc_distance(point1: tuple, point2: tuple) -> tuple:
    return point1[0] - point2[0], point1[1] - point2[1]


def is_in_grid(grid: list, point: tuple) -> bool:
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


with open('files/day8input.txt') as file:

    file = [list(line.strip()) for line in file]

antennas = load_antenna_locations(file)
print(f'Antennas: {antennas}')

antinodes = []
for signal_name in antennas:
    location_tuples = [(x, y) for x, y in product(antennas[signal_name], repeat=2) if x != y]

    for location_tuple in location_tuples:
        antenna_distance = calc_distance(location_tuple[0], location_tuple[1])
        antinode_location = (location_tuple[0][0]+antenna_distance[0], location_tuple[0][1]+antenna_distance[1])
        if is_in_grid(file, antinode_location):
            antinodes.append(antinode_location)

print(f'Antenna locations: {len(set(antinodes))}')
