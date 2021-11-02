"""
https://app.diagrams.net/?src=about#G1_ybhflNhSgdjKr9pnmvfvuAVZttaYqhU
"""
num = int(input("Ваедите трехзначное число\n"))
first_digit = num % 10
num = num // 10
second_digit = num % 10
num = num // 10
third_digit = num % 10
sum_of_digits = first_digit + second_digit + third_digit
product_of_digits = first_digit * second_digit * third_digit
print(f"сумма цифр равна {sum_of_digits}, произведение цифр равно {product_of_digits}")
