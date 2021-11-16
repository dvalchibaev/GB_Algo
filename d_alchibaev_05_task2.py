"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
BASE = 16
HEXES = ''.join([str(i) for i in range(10)] + [chr(a) for a in range(ord('A'), ord('A') + BASE - 10)])

first_hex_str = list(input('Введите первое шестнадцатиричное число\n'))
second_hex_str = list(input('Введите второе шестнадцатиричное число\n'))


def hex_sum(hex_one: list, hex_two: list) -> list:
    result_ = defaultdict(int)
    for i, chr_ in enumerate(hex_one[::-1]):
        result_[i] = HEXES.index(chr_)
    for i, chr_ in enumerate(hex_two[::-1]):
        result_[i] += HEXES.index(chr_)
    for i in range(len(result_.keys())):
        if result_[i] // BASE:
            result_[i + 1] += result_[i] // BASE
        result_[i] = result_[i] % BASE
    return [HEXES[result_[i]] for i in range(len(result_.keys()))][::-1]


def hex_mult(hex_one: list, hex_two: list) -> list:
    result_ = defaultdict(int)
    for i, chr_ in enumerate(hex_one[::-1]):
        for j, chr2_ in enumerate(hex_two[::-1]):
            result_[i + j] += HEXES.index(chr_) * HEXES.index(chr2_)
    for i in range(len(result_.keys())):
        result_[i + 1] += result_[i] // BASE
        result_[i] = result_[i] % BASE
    return [HEXES[result_[i]] for i in range(len(result_.keys()))][::-1]


print(f'Сумма чисел равна {hex_sum(first_hex_str, second_hex_str)}',
      f'Произведение чисел равно {hex_mult(first_hex_str, second_hex_str)}',
      sep='\n')