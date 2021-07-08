# l5.dz5

from random import randint
with open("dz5.txt", "w", encoding="utf-8") as f:
    string = " ".join(map(str, [randint(1, 10) for i in range(10)]))
    f.write(string)
with open("dz5.txt", "r", encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    print(sum(map(int, f.read().split())))

