from itertools import product
operators = ['+', '*', '||']  # just remove the || from the list for part one


def split(equation):
    before_colon, after_colon = equation.split(':')
    return int(before_colon.strip()), [int(num) for num in after_colon.split()]


def solve(equation):
    target, numbers = split(equation)

    def evaluate_expression(operator_combination):
        result = numbers[0]
        for i in range(len(operator_combination)):
            if operator_combination[i] == '+':
                result += numbers[i + 1]
            elif operator_combination[i] == '*':
                result *= numbers[i + 1]
            elif operator_combination[i] == '||':
                result = int(str(result) + str(numbers[i + 1]))
        return result

    # Generate all possible combinations of operators
    operator_combinations = list(product(operators, repeat=len(numbers) - 1))

    for combination in operator_combinations:
        if evaluate_expression(combination) == target:
            return target
    else:
        return 0


calibration_result = 0

with open('files/day7input.txt') as file:

    for line in file:

        calibration_result += solve(line)

print(f'Calibration result: {calibration_result}')
