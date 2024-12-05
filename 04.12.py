X, M, A, S = "X", "M", "A", "S"


def find_xmas(grid):
    rows = len(grid)
    columns = len(grid[0])
    word = "XMAS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    found_positions = []

    def is_in_grid(x, y):
        return 0 <= x < rows and 0 <= y < columns

    def search_from_point_in_direction(x, y, direction_x, direction_y):
        for i in range(len(word)):
            offset_x, offset_y = x + i * direction_x, y + i * direction_y
            if not is_in_grid(offset_x, offset_y) or grid[offset_x][offset_y] != word[i]:
                return False
        return True

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == X:
                for direction_x, direction_y in directions:
                    if search_from_point_in_direction(row, column, direction_x, direction_y):
                        found_positions.append((row, column))

    return found_positions


def find_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    found_positions = []

    def is_valid_position(x, y):
        return 0 < x < rows-1 and 0 < y < cols-1

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == A:
                if not is_valid_position(row, column):
                    continue

                nw = grid[row-1][column-1]
                ne = grid[row-1][column+1]
                sw = grid[row+1][column-1]
                se = grid[row+1][column+1]

                if ((nw == M and se == S) or (nw == S and se == M)) and ((ne == M and sw == S) or (ne == S and sw == M)):
                    found_positions.append((row, column))

    return found_positions


with open('files/day4input.txt', 'r') as file:

    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

print(f'Part 1: {len(find_xmas(lines))}')
print(f'Part 2: {len(find_mas(lines))}')
