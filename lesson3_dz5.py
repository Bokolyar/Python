# l3dz5

def my_f1():
    string = input('Введите строку чисел разделенную пробелами, q - выход из программы\n').split()
    return string


def my_f2(x):
    s = 0
    for i in x:
        if i.isdigit():
            s += int(i)
    return s


c = 0
while True:
    a = my_f1()
    b = my_f2(a)
    c += b
    print(f'сумма строки: {b}, общая сумма: {c}')
    if 'q' in a:
        break
