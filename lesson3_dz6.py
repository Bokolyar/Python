# l3dz5

def int_func(x):
    temp = x.split()
    temp1 = temp.copy()
    for i in temp:
        for j in range(len(i)):
            if ord(i[j]) < 97 or ord(i[j]) > 122:
                temp1.remove(i)
                break
    text = " ".join(temp1)
    text = text.title()
    print(text)


a = input('Введите несколько слов через пробел\n')
int_func(a)
