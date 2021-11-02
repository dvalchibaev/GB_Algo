"""
https://app.diagrams.net/?src=about#G1_ybhflNhSgdjKr9pnmvfvuAVZttaYqhU
"""
a = int(input())
b = int(input())
c = int(input())


Max = a


if b > Max:
    Max = b
if c > Max:
    Max = c


Min = a


if b < Min:
    Min = b
if c < Min:
    Min = c


print(a + b + c - Min - Max)