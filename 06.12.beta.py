import re
# this is my beta, bc the first solution took ages
# small input: 41 distinct steps, finish at row 9 col 7, 6 obstacles
# puzzle input: 5080 distinct steps, finish at row 76 col 0, 1919 obstacles

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
PATROL_ORDER = (UP, RIGHT, DOWN, LEFT)
GUARD, OBSTACLE, EMPTY = "^", "#", "."
EXIT_FOUND, NEXT_STEP, LOOP_DETECTED = range(3)

lr_shortcuts, ud_shortcuts, obstacles = [], [], []


# I know it's not the prettiest to detect north-south-, west-east-shortcuts, the position of obstacles and
# returning the starting position within one mighty method, yet it is very effective to loop only once through the
# grid, and therefore it's the way to got for now:
def load_grid_layout() -> tuple[int, int]:
    global lr_shortcuts, ud_shortcuts

    def find_free_paths(row_index, char_array, add_to_array):
        regex = r"([\.^]+)"
        matches = re.finditer(regex, ''.join(char_array))
        for match in matches:
            start, end = match.span()
            add_to_array[row_index].append((start, end-1))

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

        lr_shortcuts.append([])
        find_free_paths(i, row, lr_shortcuts)

    for i, column in enumerate(columns):
        ud_shortcuts.append([])
        find_free_paths(i, column, ud_shortcuts)

    print(f'Left-Right shortcuts: {lr_shortcuts}')
    print(f'Up-Down shortcuts: {ud_shortcuts}')
    print(f'Obstacles: {obstacles}')
    print(f'Start position: {start_position}')
    return start_position


def is_in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def is_exit_position(x, y):
    return x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1


def turn_90_degrees():
    global patrol_direction
    index = (PATROL_ORDER.index(patrol_direction) + 1) % len(PATROL_ORDER)  # adds 1 to index or resets to 0 if at end
    patrol_direction = PATROL_ORDER[index]

def calc_new_position(x:int, y:int) -> tuple[int, int]:
    """Calculate new position based on current position and direction.

    @param: x row index of current position
    @param: y column index of current position
    @return: new position coordinates x, y

    """
    if patrol_direction == UP or patrol_direction == DOWN:
        for range_tuple in ud_shortcuts[y]:
            if range_tuple[0] <= x <= range_tuple[1]:
                if patrol_direction == UP:
                    for n in range(range_tuple[0]+1, x):
                        trace.append([patrol_direction, (n, y)])
                    return range_tuple[0], y
                else:
                    for n in range(x, range_tuple[1]):
                        trace.append([patrol_direction, (n, y)])
                    return range_tuple[1], y
    else:
        for range_tuple in lr_shortcuts[x]:
            if range_tuple[0] <= y <= range_tuple[1]:
                if patrol_direction == LEFT:
                    for n in range(range_tuple[0]+1, y):
                        trace.append([patrol_direction, (x, n)])
                    return x, range_tuple[0]
                else:
                    for n in range(y, range_tuple[1]):
                        trace.append([patrol_direction, (x, n)])
                    return x, range_tuple[1]


def patrol():
    global position

    position = calc_new_position(*position)
    print(f'Patrol position: {position}')
    if [patrol_direction, position] in trace:
        print(f'Loop detected')
        return LOOP_DETECTED
    trace.append([patrol_direction, position])
    if is_exit_position(*position):
        return EXIT_FOUND
    else:
        turn_90_degrees()
        return NEXT_STEP


with open('files/day6input.txt') as file:

    grid = [list(line.strip()) for line in file]

position = load_grid_layout()
patrol_direction = UP

trace = [[patrol_direction, position]]

while patrol() == NEXT_STEP:
    pass
print(f'Trace: {trace}')
#distinct_positions = set([step[1] for step in trace])

distinct_positions = []
for step in trace:
    if step[1] not in distinct_positions:
        print(f'Step: {step[1]}')
        distinct_positions.append(step[1])

print(f"Patrol finished at {position} and after {len(distinct_positions)} steps")

