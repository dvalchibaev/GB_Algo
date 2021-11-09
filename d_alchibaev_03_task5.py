"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
# from random import randrange
#
#
# ARRAY_LENGTH = 20
# LIMIT = 100
# numbers_list = [randrange(-LIMIT, LIMIT) for _ in range(ARRAY_LENGTH)]
# Соблюдаю требование "Не используйте в основном коде (который решает поставленную задачу) константы,
#                   необходимые для генерации исходных данных."
numbers_list = [73, -31, -100, 76, -47, -25, 48, 32, -75, 94, -66, -100, -14, -76, 75, -99, 68, 69, 92, 21]
print('Дан массив', numbers_list)

max_negative_index = -1
max_negative = 0
# находим первое отрицательное число в массиве, если такое есть
for i in range(len(numbers_list)):
    if numbers_list[i] < 0:
        max_negative = numbers_list[i]
        max_negative_index = i
        break

if not max_negative:
    print("В массиве нет отрицательных чисел")
else:
    for i in range(max_negative_index + 1, len(numbers_list)):
        if max_negative < numbers_list[i] < 0:
            max_negative = numbers_list[i]
            max_negative_index = i
    print(f'Максимальное отрицательное число {max_negative}, находится в позиции {max_negative_index}')