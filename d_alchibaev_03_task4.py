"""
Определить, какое число в массиве встречается чаще всего.
"""
from collections import defaultdict
from random import randrange

ARRAY_LENGTH = 16
LIMIT = 5
numbers_list = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH)]

print('Дан массив', numbers_list)

list_instances_count = defaultdict(int)
for number in numbers_list:
    list_instances_count[number] += 1
max_count = 0
most_common_number = numbers_list[0]
for key in list_instances_count.keys():
    if list_instances_count[key] > max_count:
        max_count = list_instances_count[key]
        most_common_number = key
print(f'Чаще всего в массиве встреается число {most_common_number} (встречается {max_count} раз)')
