'''
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
'''

test1 = 'test string'
test2 = 'papa'
test3 = 'sova'


def hash_substrings(phrase: str) -> int:
    length = len(phrase)
    substrings = [phrase]
    too_long = 1_000_000
    for i in range(length):
        for j in range(i, length):
            if phrase[i:j+1] not in substrings:
                substrings.append(phrase[i:j+1])
    return (len(substrings) - 1) % too_long


print(f'Хэш строки {test1} равен {hash_substrings(test1)}')
print(f'Хэш строки {test2} равен {hash_substrings(test2)}')
print(f'Хэш строки {test3} равен {hash_substrings(test3)}')
