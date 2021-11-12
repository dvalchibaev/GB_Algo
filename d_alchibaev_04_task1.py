"""
Определить, какое число в массиве встречается чаще всего.
"""
from collections import defaultdict
from random import randrange
import cProfile
import timeit

ARRAY_LENGTH_SML, ARRAY_LENGTH_MDM, ARRAY_LENGTH_LRG = 100, 500, 1_000
LIMIT = 1000
numbers_list_sml = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH_SML)]
numbers_list_mdm = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH_MDM)]
numbers_list_lrg = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH_LRG)]


# скорость O(n), наиболее предпочтительный алгоритм из трех
def first_algo(numbers: list):
    list_instances_count = defaultdict(int)
    for number in numbers:
        list_instances_count[number] += 1
    max_count = 0
    most_common_number = numbers[0]
    for key in list_instances_count.keys():
        if list_instances_count[key] > max_count:
            max_count = list_instances_count[key]
            most_common_number = key
    return most_common_number


def test_spam(spam, inp_list):
    return spam(inp_list)


# извращенский алгоритм:) скорость O(n), но два пробега по списку (поиск максимума и затем распределение частот)
# и сильная зависимость от диапазона значений, при большом максимальном значении - сильная просадка памяти
def second_algo(numbers: list):
    max_value = numbers[0]
    for number in numbers:
        if max_value < number:
            max_value = number
    freqs = [0 for _ in range(max_value + 1)]
    most_common, max_freq = numbers[0], freqs[0]
    for number in numbers:
        freqs[number] += 1
        if max_freq < freqs[number]:
            max_freq = number
            most_common = number
    return most_common


# скорость O(n**2) (n * n/2) за счет вложенного цикла
def third_algo(numbers: list):
    freqs = [0 for _ in range(len(numbers))]
    max_freq_index = 0
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] == numbers[j]:
                freqs[j] += 1
            if freqs[j] > freqs[max_freq_index]:
                max_freq_index = j
    return numbers[max_freq_index]

# print(f'Размер массива {ARRAY_LENGTH}, числа в диапазоне [0, {LIMIT}), 100 итераций')
# print(timeit.timeit("first_algo(numbers_list)", number=100, globals=globals()))  # 0.0035371060002944432
# print(timeit.timeit("second_algo(numbers_list)", number=100, globals=globals())) # 0.004069144999903074
# print(timeit.timeit("third_algo(numbers_list)", number=100, globals=globals()))  # 0.8487059290000616
#
# print(f'Размер массива {ARRAY_LENGTH}, числа в диапазоне [0, {LIMIT}), 500 итераций')
# print(timeit.timeit("first_algo(numbers_list)", number=500, globals=globals()))  # 0.017497430999810604
# print(timeit.timeit("second_algo(numbers_list)", number=500, globals=globals())) # 0.021376602999680472
# print(timeit.timeit("third_algo(numbers_list)", number=500, globals=globals()))  # 4.223674614999709
#
# print(f'Размер массива {ARRAY_LENGTH}, числа в диапазоне [0, {LIMIT}), 1 000 итераций')
# print(timeit.timeit("first_algo(numbers_list)", number=1000, globals=globals()))  # 0.04573241300022346
# print(timeit.timeit("second_algo(numbers_list)", number=1000, globals=globals())) # 0.05415318300038052
# print(timeit.timeit("third_algo(numbers_list)", number=1000, globals=globals()))  # 14.094485395999982


#cProfile.run('first_algo(numbers_list_lrg * 10_000)')

'''
    Вызов при размере массива 10 000 000
         5 function calls in 1.090 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.055    0.055    1.090    1.090 <string>:1(<module>)
        1    1.036    1.036    1.036    1.036 d_alchibaev_04_task1.py:17(first_algo)
        1    0.000    0.000    1.090    1.090 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
'''
# cProfile.run('second_algo(numbers_list_lrg * 10000)')
'''
    Вызов при размере массива 10 000 000
         5 function calls in 1.601 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.053    0.053    1.601    1.601 <string>:1(<module>)
        1    1.548    1.548    1.548    1.548 d_alchibaev_04_task1.py:36(second_algo)
        1    0.000    0.000    0.000    0.000 d_alchibaev_04_task1.py:41(<listcomp>)
        1    0.000    0.000    1.601    1.601 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('third_algo(numbers_list_lrg * 25)')
