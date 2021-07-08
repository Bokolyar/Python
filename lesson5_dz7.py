# l5.dz7
import json


structure1 = {}
structure2 = {}
spisok = []
n = 0
s = 0
with open("text_7.txt", "r", encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line:
            break
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            n += 1
            s += profit
        structure1[line[0]] = profit
structure2["average_profit"] = s/n
spisok = [structure1, structure2]
print(spisok)
with open("dz7.json", "w", encoding='utf-8') as j_f:
    json.dump(spisok, j_f, ensure_ascii=False, indent=4)
