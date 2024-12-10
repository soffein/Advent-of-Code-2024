with open('files/day10input.txt') as input_file:

    grid = [list(line.strip()) for line in input_file]

print(grid)
print(f'Grid has {len(grid)} rows and {len(grid[0])} columns')