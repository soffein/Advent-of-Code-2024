
def find_starts():
    global grid, starting_positions
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 0:
                starting_positions.append((x, y))


with open('files/day10input.txt') as input_file:

    grid = [[int(char) for char in line.strip()] for line in input_file]

starting_positions = []
find_starts()

print(f'Grid: {grid}')
print(f'Starting_positions: {starting_positions}')
print(f'Grid has {len(grid)} rows and {len(grid[0])} columns')