from datetime import datetime

SPACE = '.'
file_content = []
defragmented_content = []


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_file_content() -> list:
    global instruction, file_content
    file_index = 0

    for i, char in enumerate(instruction):
        factor = int(char)
        if is_even(i):
            character = file_index
            file_index += 1
        else:
            character = SPACE
        file_content.extend([character] * factor)

    return file_content


def find_index_of_last_number(stop_index) -> int:
    index = 0
    for i in range(len(defragmented_content)-1, stop_index, -1):
        if isinstance(defragmented_content[i], int):
            index = i
            break
    return index


def switch_position() -> bool:
    switched = False
    first_space_index = defragmented_content.index(SPACE)
    last_number_index = find_index_of_last_number(first_space_index)
    if first_space_index < last_number_index:
        defragmented_content[first_space_index], defragmented_content[last_number_index] = defragmented_content[last_number_index], defragmented_content[first_space_index]
        switched = True
    return switched


def defrag():
    global defragmented_content
    defragmented_content = list(file_content)
    while switch_position():
        pass


start_time = datetime.now()
with open('files/day9input.txt') as input_file:

    instruction = input_file.readline()

generate_file_content()
defrag()
end_time = datetime.now()
print(defragmented_content)
print(f'Execution time: {(end_time - start_time).total_seconds()} s')
