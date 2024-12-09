SPACE = '.'


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_file_content() -> list:
    global instruction
    file_content = []
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

with open('files/day9input.txt') as input_file:

    instruction = input_file.readline()

generated_content = generate_file_content()
print(generated_content)
