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


def walk_the_trail(position: list, visited: set) -> list:
    trails = []
    stack = [(position, [position])]
    while stack:
        current_pos, path = stack.pop()
        if grid[current_pos[0]][current_pos[1]] == 9:
            trails.append(path)
        for neighbor in check_neighbors(current_pos[0], current_pos[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return trails


def find_trails():
    global starting_positions, paths
    for position in starting_positions:
        visited = set()
        visited.add(position)
        paths.extend(walk_the_trail(position, visited))


def build_trail_scores():
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
build_trail_scores()

print(f'Valid Trails: {paths}')
print(f'Grid: {grid}')
print(f'Starting_positions: {starting_positions}')
print(f'Grid has {len(grid)} rows and {len(grid[0])} columns')