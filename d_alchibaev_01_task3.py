"""
https://app.diagrams.net/?src=about#G1_ybhflNhSgdjKr9pnmvfvuAVZttaYqhU
"""
x1, y1, x2, y2 = (float(x) for x in input("Введите координаты первой и второй точки через пробел\n").split(' '))

if x1 == x2:
    print("Некорректный ввод")
else:
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    print(f"y = {k} x + {b}")
