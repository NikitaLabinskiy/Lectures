# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

number = 1
result = 1

while number <= 5:
    if number == 0:
        break
    result *= number
    number += 1
print(result)

result2 = 1

for i in range(1, 6):
    result2 *= i
print(result2, 'another')
