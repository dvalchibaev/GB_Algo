'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''
from random import randrange

LIMIT_LOW = -100
LIMIT_HIGH = 100
ARRAY_M = 7
ELEMENTS_NUM = 2 * ARRAY_M + 1
unsorted_list = [randrange(LIMIT_LOW, LIMIT_HIGH) for _ in range(ELEMENTS_NUM)]


def find_median(unsorted_data: list) -> int:
    sorted_data = heap_sort(unsorted_data)
    if len(sorted_data) % 2:
        return sorted_data[len(sorted_data) // 2]
    return 0.5 * (sorted_data[len(sorted_data) // 2] + sorted_data[len(sorted_data) // 2 + 1])


def is_sorted(data:list) -> bool:
    for i in range(1, len(data)):
        if data[i-1] > data[i]:
            return False
    return True


def heap_sort(data: list) -> list:
    if is_sorted(data):
        return data
    length = len(data)
    result_ = create_heap(data)
    for i in range(1, length):
        result_[0], result_[-i] = result_[-i], result_[0]
        sift(result_, 0, length - i - 1)
    return result_


def create_heap(data_list: list):
    result_ = data_list.copy()
    if len(result_) <= 1:
        return result_
    start_index = (len(result_) - 1) // 2
    for i in range(start_index)[::-1]:
        sift(result_, i, len(result_) - 1)
    return result_


# def order(number: int) -> int:
#     return len(bin(number)) - 2
#
#
# def print_heap(heap: list):
#     power = order(len(heap))
#     for i in range(power):
#         print('\t' * (power - i - 1), heap[2 ** i - 1: min(2 ** (i + 1) - 1, len(heap))])


def left_child_index(index: int):
    return 2 * index + 1


def sift(heap, start, end):
    root = start
    while left_child_index(root) <= end:
        child = left_child_index(root)
        spam = root
        if heap[spam] < heap[child]:
            spam = child
        if child + 1 <= end and heap[spam] < heap[child + 1]:
            spam = child + 1
        if spam != root:
            heap[root], heap[spam] = heap[spam], heap[root]
            root = spam
        else:
            break


sorted_heap = heap_sort(unsorted_list)
print(f'Исходный массив данных из {ELEMENTS_NUM} элементов')
print(unsorted_list)
print('Отсортированный массив')
print(sorted_heap)
print('Медиана в массиве данных равна:')
print(find_median(sorted_heap))