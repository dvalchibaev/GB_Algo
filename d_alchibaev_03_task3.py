"""

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""
# from random import randrange


# ARRAY_LENGTH = 16
# LIMIT = 100
# numbers_list = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH)]
# Соблюдаю требование "Не используйте в основном коде (который решает поставленную задачу) константы,
#                   необходимые для генерации исходных данных."
numbers_list = [89, 9, 67, 26, 27, 6, 66, 99, 30, 22, 65, 59, 74, 65, 72, 92]
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
numbers_list[max_index] = min_element
numbers_list[min_index] = max_element
print(f'Максимальный элемент = {max_element} в позиции {max_index}; '
      f'минимальный элемент = {min_element} в позиции {min_index}\n'
      f'Результат операции {numbers_list}')
