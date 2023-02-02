# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

number = int(input('Введите число: '))
number1 = 1
number2 = 1

for i in range (0, number):
    if number < 0:
        print(-1)
    elif number == 0:
        print(1)
    elif number == 1:
        print(1, 2)
    else:
        number_sum = number1 + number2
        number1 = number2
        number2 = number_sum
        if number == number2:
            print(i + 4)
            print(number)
            break
        elif number < number2:
            print(-1)
            break

