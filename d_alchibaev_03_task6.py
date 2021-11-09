"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randrange


ARRAY_LENGTH = 16
LIMIT = 100
numbers_list = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH)]

print('Дан массив', numbers_list)


max_element, min_element = numbers_list[0], numbers_list[0]
max_index, min_index = (0, 0)
for i in range(len(numbers_list)):
    if numbers_list[i] > max_element:
        max_element = numbers_list[i]
        max_index = i
    if numbers_list[i] < min_element:
        min_element = numbers_list[i]
        min_index = i

if min_index > max_index:
    start_pos = max_index
else:
    start_pos = min_index
end_pos = max_index + min_index - start_pos
sum_of_numbers = 0
for i in range(start_pos + 1, end_pos):
    sum_of_numbers += numbers_list[i]
print(f'Максимальный элемент: {max_element}, минимальный элемент: {min_element}, '
      f'сумма элементов между ними: {sum_of_numbers}')
