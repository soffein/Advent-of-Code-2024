rules = []
print_instructions = []


def validate(pages):

    for i, page in enumerate(pages):
        for rule in rules:
            if page == rule[0]:
                try:
                    index = pages.index(rule[1])
                    if i > index:
                        pages[i], pages[i - 1] = pages[i - 1], pages[i]
                        validate(pages)
                        return False
                except ValueError:
                    pass

    return True


def get_middle_item(lst):

    return lst[(len(lst) // 2)]


with open('files/day5input.txt') as file:

    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            print_instructions.append(list(map(int, line.split(","))))

was_always_valid, is_now_valid = [], []

for instruction in print_instructions:

    (was_always_valid if validate(instruction) else is_now_valid).append(instruction)

print(f'Sum of already valid instructions: {sum(get_middle_item(instruction) for instruction in was_always_valid)}')
print(f'Sum of now valid instructions: {sum(get_middle_item(instruction) for instruction in is_now_valid)}')
