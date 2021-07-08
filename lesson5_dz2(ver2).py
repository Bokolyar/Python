# l5.dz2(ver2)

with open("dz2.txt", "a+", encoding="utf-8") as f:
    f.write("Шла Саша по шоссе\nи сосала сушку\n")
    f.seek(0)
    print(f.read())
    f.seek(0)
    n = 0
    while True:
        line = f.readline()
        if not line:
            break
        n += 1
        print(f"{n}-я строка, кол-во слов: {len(line.split())}")
print(f"Всего в файле {n} строк")




