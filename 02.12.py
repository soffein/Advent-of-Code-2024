import csv


def is_safe(record):
    record = list(map(int, record))

    if record[0] < record[1]:
        for i in range(1, len(record)):
            if not (record[i] - 3 <= record[i - 1] <= record[i] - 1):
                return False
    else:
        for i in range(1, len(record)):
            if not (record[i] + 1 <= record[i - 1] <= record[i] + 3):
                return False

    return True


def can_be_safe(record):

    for i, value in enumerate(record):

        dampened_array = list(record)
        dampened_array.pop(i)
        if is_safe(dampened_array):
            return True
    return False


number_of_save_reports = 0
number_of_save_reports_with_dampener = 0

with open('files/day2input.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=' ')
    for i, row in enumerate(csv_reader, start=1):

        if is_safe(row):
            number_of_save_reports += 1

        elif can_be_safe(row):
            number_of_save_reports_with_dampener += 1

print(f'Number of save reports: {number_of_save_reports}')
print(f'Number of save reports with dampener: {number_of_save_reports_with_dampener}')
print(f'Total number of possibly save reports: {number_of_save_reports+number_of_save_reports_with_dampener}')
