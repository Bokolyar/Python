# l2.dz2

spisok = list(input('Введите список: '))

# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 3]
spisok1 = []
for i in range(0, len(spisok)-1, 2):
    spisok1.append(spisok[i+1])
    spisok1.append(spisok[i])

spisok1.append(spisok[-1]) if len(spisok) % 2 != 0 else None

print(spisok1)
