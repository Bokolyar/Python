# l2.dz5

i = 1
spisok = [7, 5, 3, 3, 2]
while i != 0:
    element = int(input('Введите элемент рейтинга от 1 до 9 или 0 для завершения программы: '))
    if element == 0:
        break
    if element <= spisok[-1]:
        spisok.append(element)
        print(spisok)
        continue
    for j in range(len(spisok)):
        if element > spisok[j]:
            # spisok.insert(j, str(element))
            spisok.insert(j, element)
            break
    print(spisok)
