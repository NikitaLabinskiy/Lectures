# Тип данных
# int, floar, boolean, str, list, None
# value = None
# a = 123
# b = 12.34
# s = 'python\'s synt'
# s2 = "python's synt"

# print(type(a)) # интерполяция
# print(type(b))
# print(type(value))
# print(s)
# print(s2)
# print('{2} - {0} - {1}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# print('Ввеедите a') # целые числа
# a = int(input())
# print('Ввеедите b')
# b = int(input())
# print(f'{a} + {b} = {a + b}')

# print('Ввеедите c') # вещественные числа
# c = float(input())
# print('Ввеедите d')
# d = float(input())
# print(f'{c} + {d} = {c * d}')

# print('Ввеедите x')  # целые и вещественные числа
# x = float(input())
# print('Ввеедите z')
# z = int(input())
# y = round(x * z, 3)
# print(y)

# Логическое операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# s = [1, 2, 3, 4, 5, 6]
# result = s[1] % 2 == 0
# print(result)

# Операторы

# if condition:
#     operator1
#     operator2
#     operator3
# else condition:
#     operator1
#     operator2

# while condition:
#     operator1
#     operator2
#     operator3

# for i in smth:

# for i in 1, 2, 3, 4, 5, 6:
#     print(i**2)


# Немного о строках
text = 'какой нибудь текст'
print(text)
print(len(text))              # количество символов
print('какой' in text)        # проверка наличия True
print(text.isdigit())     
print(text.islower()) 
print(text.replace('какой','Какой')) 

