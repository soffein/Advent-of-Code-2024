import bisect

array_a = []
array_b = []

with open('files/day1input.csv', 'r') as file:

    for row in file.readlines():

        a, b = row.split()
        bisect.insort(array_a, int(a))
        bisect.insort(array_b, int(b))

distance = 0
similarity = 0

for i, value in enumerate(array_a):
    distance += abs(array_a[i] - array_b[i])
    similarity += array_a[i] * array_b.count(array_a[i])

print(f'Distance between array_a and array_b is {distance:,}')
print(f'Similarity between array_a and array_b is {similarity:,}')
