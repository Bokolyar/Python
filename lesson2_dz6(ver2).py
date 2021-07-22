# l2.dz6 ver.2

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
        sp_dict = list(zip(*structure))[1]
        for j in list(structure[0][1]):
            a = [i[j] for i in sp_dict]
            a = list(set(a))
            analytics.update({j: a})
        print(analytics)
    elif menu == 4:
        print('Конец')
        break
    else:
        print("Вы ввели недопустимое значение!")
        continue
