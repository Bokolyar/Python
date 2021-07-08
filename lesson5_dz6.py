# l5.dz6

structure = {}

with open("text_6.txt", "r", encoding="utf-8") as f:
    while True:
        s = 0
        line = f.readline()
        if not line:
            break
        test = line.split()
        for el in test[1:]:
            a = ''
            for i in range(len(el)):
                if el[i].isdigit():
                    a += el[i]
            if a != '':
                s += int(a)
        structure[test[0][0:-1]] = s
print(structure)
