# # l2.dz5

my_list = [7, 5, 3, 3, 2]
while True:
    new_el = int(input('Введите элемент рейтинга от 1 до 9 или 0 для завершения программы: '))
    if new_el == 0:
        break
    elif new_el <= my_list[-1]:
        my_list.append(new_el)
        print(my_list)
    else:
        for i in range(len(my_list)):
            if new_el >= my_list[i]:
                my_list.insert(i, new_el)
                break
        print(my_list)


