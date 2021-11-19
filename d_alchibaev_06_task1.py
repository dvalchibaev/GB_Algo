"""
Определить, какое число в массиве встречается чаще всего.
"""
# в этот раз подробно погрузиться в задачу получится только в выходные,
# поэтому пока прикладываю простенькое решение
from collections import defaultdict
from random import randrange
import sys

ARRAY_LENGTH = 10_000
LIMIT = 100_000_000
numbers_list_sml = [randrange(0, LIMIT) for _ in range(ARRAY_LENGTH)]


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

    # занятая память под капотом пропускается, на выходе только результат расчета
    items = [item_ for item_ in locals() if '__' not in str(item_)]
    size_total = 0
    print(f"\nПамять использованных объектов:")
    for i in items:
        size_ = sys.getsizeof(i)
        print(f'Имя объекта {str(i)}, его размер {size_}')
        size_total += size_
    print(f"Итого использовано памяти {size_total}")
    return most_common_number


# извращенский алгоритм:) скорость O(n), но два пробега по списку (поиск максимума и затем распределение частот)
# и сильная зависимость от диапазона значений,
# при большом максимальном значении - сильная просадка памяти (при наивной проверке - оказалось, что не особо:))
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

    # занятая память под капотом пропускается, на выходе только результат расчета
    items = [item_ for item_ in locals() if '__' not in str(item_)]
    size_total = 0
    print(f"\nПамять использованных объектов:")
    for i in items:
        size_ = sys.getsizeof(i)
        print(f'Имя объекта {str(i)}, его размер {size_}')
        size_total += size_
    print(f"Итого использовано памяти {size_total}")
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

    # занятая память под капотом пропускается, на выходе только результат расчета
    items = [item_ for item_ in locals() if '__' not in str(item_)]
    size_total = 0
    print(f"\nПамять использованных объектов:")
    for i in items:
        size_ = sys.getsizeof(i)
        print(f'Имя объекта {str(i)}, его размер {size_}')
        size_total += size_
    print(f"Итого использовано памяти {size_total}")
    return numbers[max_freq_index]


first_algo(numbers_list_sml)
# defaultdict ест немного больше памяти, чем стандартные списки, поскольку,
# я предполагаю, есть дополнительные затраты на ключи
"""
Память использованных объектов:
Имя объекта numbers, его размер 56
Имя объекта list_instances_count, его размер 69
Имя объекта number, его размер 55
Имя объекта max_count, его размер 58
Имя объекта most_common_number, его размер 67
Имя объекта key, его размер 52
Итого использовано памяти 357
"""
second_algo(numbers_list_sml)
# Используются вспомогательные списки, которые отнимают память, отдако немного меньше, чем defaultdict
"""
Память использованных объектов:
Имя объекта numbers, его размер 56
Имя объекта max_value, его размер 58
Имя объекта number, его размер 55
Имя объекта freqs, его размер 54
Имя объекта most_common, его размер 60
Имя объекта max_freq, его размер 57
Итого использовано памяти 340
"""
third_algo(numbers_list_sml)
# Используется меньше вспомогательных объектов и вспомогательных типов как defaultdict,
# есть крошечный выигрыш в памяти, но считает безумно медленно
"""
Память использованных объектов:
Имя объекта numbers, его размер 56
Имя объекта freqs, его размер 54
Имя объекта max_freq_index, его размер 63
Имя объекта i, его размер 50
Имя объекта j, его размер 50
Итого использовано памяти 273
"""
