PATROL = ((-1, 0), (0, 1), (1, 0), (0, -1)) # it's: up, right, down, left
GUARD = "^"
OBSTACLE = "#"


def find_start_position():
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == GUARD:
                return row, column


def is_in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def is_exit_position(x, y):
    return x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1


def is_obstacle(x, y):
    a = x + PATROL[patrol_direction][0]
    b = y + PATROL[patrol_direction][1]
    item = grid[a][b]
    return item == OBSTACLE


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
    steps.append(position)
    if is_exit_position(*position):
        return False
    else:
        return True


with open('files/day6input.txt') as file:

    grid = [list(line.strip()) for line in file]

steps = []
patrol_direction = 0
position = find_start_position()
steps.append(position)

while patrol():
    pass

print(f"Patrol finished at {position} and after {len(set(steps))} steps")

