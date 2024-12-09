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
        file_content.append((factor, character))

    return file_content


def find_matching_space(stop_index, block_length) -> int:
    index = stop_index
    for i in range(stop_index):
        if defragmented_content[i][1] is SPACE and defragmented_content[i][0] >= block_length:
            index = i
            break
    return index


def switch_position(block_index):
    current_block = defragmented_content[block_index]
    switch_index = find_matching_space(block_index, current_block[0])
    if defragmented_content[block_index][1] == SPACE:
        return
    elif switch_index < block_index:
        space = defragmented_content[switch_index]
        block = defragmented_content[block_index]
        # first, put the block on the space position:
        defragmented_content[switch_index] = block
        # then, update the former position with spaces
        defragmented_content[block_index] = (block[0], SPACE)
        # last, see if we need to fill up with space characters
        space_insert_length = space[0] - block[0]
        if space_insert_length != 0:
            insert_space = (space_insert_length, SPACE)
            defragmented_content.insert(switch_index+1, insert_space)


def defrag():
    global defragmented_content
    defragmented_content = list(file_content)

    for i in range(len(defragmented_content)-1, 1, -1):
        switch_position(i)


def build_checksum() -> int:
    checksum = 0
    flattened_array = [value for count, value in defragmented_content for _ in range(count)]

    for i, value in enumerate(flattened_array):
        if value == SPACE:
            continue
        else:
            checksum += value * i

    return checksum


start_time = datetime.now()
with open('files/day9input.txt') as input_file:

    instruction = input_file.readline()

generate_file_content()
defrag()
end_time = datetime.now()
print(f'Checksum: {build_checksum()}')
print(f'Execution time: {(end_time - start_time).total_seconds()} s')
