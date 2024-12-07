import re
# this is my beta, bc the first solution took ages
# small input: 41 distinct steps, finish at row 9 col 7, 6 obstacles
# puzzle input: 5080 distinct steps, finish at row 76 col 0, 1919 obstacles

PATROL = ((-1, 0), (0, 1), (1, 0), (0, -1))  # it's: up, right, down, left
GUARD = "^"
OBSTACLE = "#"
EMPTY = "."
EXIT_FOUND = 0
LOOP_DETECTED = 1
NEXT_STEP = 2

we_shortcuts, ns_shortcuts, obstacles = [], [], []


# I know it's not the prettiest to detect north-south-, west-east-shortcuts, the position of obstacles and
# returning the starting position within one mighty method, yet it is very effective to loop only once through the
# grid, and therefore it's the way to got for now:
def load_grid_layout() -> tuple[int, int]:

    def find_free_paths(row_index, char_array, add_to_array):
        regex = r"([\.^]+)"
        matches = re.finditer(regex, ''.join(char_array))
        for match in matches:
            start, end = match.span()
            add_to_array.append([row_index, (start, end-1)])

    columns = ['' for _ in grid[0]]
    start_position = (0, 0)

    for i, row in enumerate(grid):
        for j, point in enumerate(row):
            # TODO: not sure yet, if we need that array or if an == OBSTACLE check is better; delete this if so
            if point == OBSTACLE:
                obstacles.append((i, j))
            elif point == GUARD:
                start_position = (i, j)
            columns[j] += point

        find_free_paths(i, row, we_shortcuts)

    for i, column in enumerate(columns):
        find_free_paths(i, column, ns_shortcuts)

    print(f'West-East shortcuts: {we_shortcuts}')
    print(f'North-South shortcuts: {ns_shortcuts}')
    print(f'Obstacles: {obstacles}')
    print(f'Start position: {start_position}')
    return start_position


def is_in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def is_exit_position(x, y):
    return x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1


def determine_direction():
    global patrol_direction
    if patrol_direction < len(PATROL)-1:
        patrol_direction += 1
    else:
        patrol_direction = 0


def calc_next_step(x, y):

    nx = x + PATROL[patrol_direction][0]
    ny = y + PATROL[patrol_direction][1]

    if grid[nx][ny] == OBSTACLE:
        determine_direction()
        return calc_next_step(x, y)

    return nx, ny


def patrol():
    global position

    position = calc_next_step(*position)
    if [patrol_direction, position] in steps:
        return LOOP_DETECTED
    steps.append([patrol_direction, position])
    if is_exit_position(*position):
        return EXIT_FOUND
    else:
        return NEXT_STEP


with open('files/day6input.txt') as file:

    grid = [list(line.strip()) for line in file]

position = load_grid_layout()
patrol_direction = 0

steps = [[patrol_direction, position]]

while patrol() == NEXT_STEP:
    pass

distinct_positions = set([step[1] for step in steps])
print(f"Patrol finished at {position} and after {len(distinct_positions)} steps")

