# Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

spisok = [1, 2, 3, 4, 5]
number = 3
slice_spisok1 = spisok[number:]
slice_spisok2 = spisok[:number]
result_spisok = slice_spisok1 + slice_spisok2
print(result_spisok)
    