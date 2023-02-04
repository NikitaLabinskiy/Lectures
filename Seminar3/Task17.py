# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
spisok = [1, 1, 2, 0, -1, -1, -1, 3, 4, 4]

spisok2 = [0,0,0,0,0,0,0,0,0]
# index1 = 0
# for i in range(9):
#     if spisok[i] != spisok[i + 1]:
#         spisok2.append(spisok[i])
#     else:
#         continue
# spisok2.sort()
# print (spisok2)
# print (len(spisok2))

for i in range(9):
    if spisok[i] != spisok2[i]:
        spisok2.append(spisok[i])
    else:
        continue
print(spisok2)
print (len(spisok2))

