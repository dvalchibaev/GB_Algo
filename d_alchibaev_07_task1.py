'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''
from random import randrange

LIMIT_LOW = -100
LIMIT_HIGH = 100
ELEMENTS_NUM = 20
unsorted_list = [randrange(LIMIT_LOW, LIMIT_HIGH) for _ in range(ELEMENTS_NUM)]


def bubble_sort(list_to_sort: list) -> list:
    result_ = list_to_sort.copy()
    print('START')
    for i in range(len(list_to_sort) - 1):
        swapped = False
        for j in range(len(list_to_sort) - i - 1):
            if result_[j + 1] > result_[j]:
                result_[j], result_[j + 1] = result_[j + 1], result_[j]
                swapped = True
        if not swapped:
            break
        print(result_)
    return result_


def sort_test(sorted_l: list) -> bool:
    test = True
    for i in range(len(sorted_l) - 1):
        if sorted_l[i] < sorted_l[i + 1]:
            test = False
    if test:
        print('Test Ok')
    else:
        print('Test Not ok')
    return test


sorted_list = bubble_sort(unsorted_list)
double_sort = bubble_sort(sorted_list)
# sort_test(sorted_list)
print(f'Диапазов значений в массие [{LIMIT_LOW}, {LIMIT_HIGH}), размер массива - {ELEMENTS_NUM} элементов')
print(f'Исходный массив \t \t {unsorted_list}')
print(f'Отсортированный массив \t {sorted_list}')
