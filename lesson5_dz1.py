# l5.dz1

f = open("dz1.txt", "w", encoding="utf-8")
print("Input text:")
str = input("")
while str != "":
    f.write(f"{str}\n")
    str = input()
print("Введенный вами текст сохранен в файле dz1.txt")
f.close()
