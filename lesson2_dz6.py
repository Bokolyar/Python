# l2.dz6

# 1-й вариант: функция удаления задвоенных элементов, через перевод в множество и обратно
def convert(list1):
    return list(set(list1))


# 2-й вариант: функция удаления задвоенных элементов, путем сравнения
def convert1(list1):
    for elem in list1:
        if list1.count(elem) >= 2:
            list1.remove(elem)
    return list1


# формируем базовую структуру, чтобы упростить ввод
structure = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})
]

# делаем меню для программы
while True:
    menu = int(input("Меню: 1 - добавить товар, 2 - посмотреть список товаров, 3 - посмотреть аналитику, 4 - выход \n"))
    if menu == 1:
        name = input("название: ")
        price = int(input("цена: "))
        count = int(input("количество: "))
        unit = input("ед: ")
        structure.append((len(structure) + 1, {"название": name, "цена": price, "количество": count, "ед": unit}))
    elif menu == 2:
        for i in range(len(structure)):
            print(f'{structure[i][0]}: {structure[i][1]}')
    elif menu == 3:
        analytics = {}
        temp_list = [[], [], [], []]
        # формируем список, каждый элемент которого список характеристик
        for i in range(len(structure[0][1])):
            for j in range(len(structure)):
                temp_list[i].append(structure[j][1][list(structure[0][1])[i]])
        # удаляем дубликатыи задаем структуру словаря для аналитики
        for i in range(len(temp_list)):
            temp_list[i] = convert1(temp_list[i])
            analytics.update({list(structure[0][1])[i]: temp_list[i]})
        print(analytics)
    elif menu == 4:
        print('Конец')
        break
    else:
        print("Вы ввели недопустимое значение!")
        continue
