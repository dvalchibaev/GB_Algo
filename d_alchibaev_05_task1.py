"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
import collections
QUARTER = 0.25

corps_amount = int(input('Введите количество предприятий\n'))
corps = collections.defaultdict(float)
for i in range(corps_amount):
    corps_name_ = input(f'Введите название {i + 1}-го предприятия\n')
    for j in range(4):
        corps[corps_name_] += QUARTER * float(input(f'Введите прибыль за {j + 1}-й квартал\n'))


mean_ = 0.
for key in corps.keys():
    mean_ = corps[key] / corps_amount

print(f'Средний доход предприятий {mean_}')

print(f'Предприятия с доходом выше среднего {[key for key in corps.keys() if corps[key] > mean_]} \n')

print(f'Предприятия с доходом ниже среднего {[key for key in corps.keys() if corps[key] < mean_]} \n')
