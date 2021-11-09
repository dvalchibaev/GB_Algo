"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
from random import randrange


ARRAY_LENGTH = 16
LIMIT = 100
numbers_list = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH)]

print('Дан массив', numbers_list)

even_positions = []
for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_positions.append(i)

print('Результат операции ', even_positions)
