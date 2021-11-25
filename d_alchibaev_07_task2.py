"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import random

LIMIT_LOW = 0
LIMIT_HIGH = 50
ELEMENTS_NUM = 11
unsorted_l = [(LIMIT_HIGH - LIMIT_LOW) * random() for _ in range(ELEMENTS_NUM)]


def merge_sort(unsorted_list: list) -> list:
    result_ = unsorted_list.copy()
    list_len = len(result_)
    if list_len < 2:
        return result_
    list_l = merge_sort(result_[:list_len // 2])
    list_r = merge_sort(result_[list_len // 2:])
    if list_l[-1] < list_r[0]:
        result_ = list_l.copy()
        result_.extend(list_r)
        return result_
    if list_r[-1] < list_l[0]:
        result_ = list_r.copy()
        result_.extend(list_l)
        return result_
    result_ = [0] * list_len
    left, right = 0, 0
    for i in range(list_len):
        if right == len(list_r):
            result_[i] = list_l[left]
            left += 1
        elif left == len(list_l):
            result_[i] = list_r[right]
            right += 1
        elif list_l[left] <= list_r[right]:
            result_[i] = list_l[left]
            left += 1
        else:
            result_[i] = list_r[right]
            right += 1
    return result_


def sort_test(sorted_l: list) -> bool:
    test = True
    for i in range(len(sorted_l) - 1):
        if sorted_l[i] >= sorted_l[i + 1]:
            test = False
    if test:
        print('Test Ok')
    else:
        print('Test Not ok')
    return test


sorted_l = merge_sort(unsorted_l)
print(f'Исходный массив {unsorted_l}')
print(f'Отсортированный массив {sorted_l}')
sort_test(sorted_l)
