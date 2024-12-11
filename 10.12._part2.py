NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def load_starts():
    global grid, starting_positions
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 0:
                starting_positions.append((x, y))


def check_neighbors(x: int, y: int) -> list:
    global grid

    valid_trail_steps = []
    for neighbor in NEIGHBORS:
        if (0 <= x + neighbor[0] < len(grid) and 0 <= y + neighbor[1] < len(grid[0]) and
                grid[x + neighbor[0]][y + neighbor[1]] == grid[x][y] + 1):
            valid_trail_steps.append((x + neighbor[0], y + neighbor[1]))
    return valid_trail_steps


def walk_the_trail(position: list) -> list:
    trails = [position]
    for neighbor in check_neighbors(position[0], position[1]):
        trails.extend(walk_the_trail(neighbor))
    return trails


def find_trails():
    global starting_positions, paths
    for position in starting_positions:
        paths.append(walk_the_trail(position))


def get_total_ratings():
    total_rating = 0
    for trail in paths:
        for position in trail:
            if grid[position[0]][position[1]] == 9:
                total_rating += 1
    print(f'Sum of als ratings is {total_rating}')


def get_total_trail_scores():
    global paths
    trailhead_scores = {}
    for trail in paths:
        trailhead = trail[0]
        if trailhead not in trailhead_scores:
            trailhead_scores[trailhead] = 0
        trailhead_scores[trailhead] += 1
    print(f'Sum of scores is {sum(trailhead_scores.values())}')


with open('files/day10input.txt') as input_file:

    grid = [[int(char) for char in line.strip()] for line in input_file]

starting_positions = []
load_starts()

paths = []
find_trails()
get_total_trail_scores()
get_total_ratings()

print(f'Valid Trails: {paths}')