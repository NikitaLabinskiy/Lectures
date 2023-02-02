# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

number = input()
number1 = 1
number2 = 1

index = 2
for i in range (0, number):
    number_sum = number1 + number2
    number1 = number2
    number2 = number_sum
    if number2 == number:
        print()
