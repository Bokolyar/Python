# l5.dz3

with open("text_3.txt", "r", encoding="utf-8") as f:
    n = 0
    s = 0
    print("Сотрудники с доходом менее 20000:")
    while True:
        line = f.readline().split()
        if not line:
            break
        if float(line[1]) < 20000:
            print(line[0])
        n += 1
        s += float(line[1])
    print(f"Средний доход всех сотрудников: {s/n}")
