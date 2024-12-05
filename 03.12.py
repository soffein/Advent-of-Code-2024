import re

PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
DO = "do()"
DONT = "don't()"


def build_sum_of_products(text):

    return sum(int(m.group(1)) * int(m.group(2)) for m in re.finditer(PATTERN, text, re.MULTILINE))


def remove_dont_parts(text):

    parts = text.split(DONT)
    clean_string = parts[0]

    for part in parts[1:]:
        if DO in part:
            split_value = part.split(DO, 1)
            if len(split_value) > 1:
                clean_string += split_value[1]
    return clean_string


with open('files/day3input.txt', 'r') as file:

    text = file.read()

print(f"Sum of products: {build_sum_of_products(text)}")
print(f"Sum of enabled products: {build_sum_of_products(remove_dont_parts(text))}")
