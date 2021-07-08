# l5.dz2

f = open("dz1.txt", "r", encoding="utf-8")
print(f.read())
f.seek(0)
string = f.readlines()
print(f"Кол-во строк в файле: {len(string)}")
f.seek(0)
n = 1
for i in f.readlines():
    print(f"{n}-я строка, кол-во слов: {len(i.split())}")
    n += 1
f.close()
