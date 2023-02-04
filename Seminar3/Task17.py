# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

spisok = [1, 1, 2, 0, -1, -1, -1, 3, 4, 4]
spisok2 = []

for i in range(10):
    if spisok[i] not in spisok2:
        spisok2.append(spisok[i])
    else:
        continue
print(spisok2)
print (len(spisok2))
