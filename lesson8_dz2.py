class MyOwnErr(Exception):
    def __init__(self, txt):
        print(txt)


print(f'Вычисляем a/b')
while True:
    try:
        a = float(input('Введите 1-е число: a = '))
    except ValueError:
        print(f'Вы ввели не число')
        continue
    else:
        break
while True:
    try:
        b = float(input('Введите 2-е число: b = '))
        if b == 0:
            raise MyOwnErr('Деление на 0 невозможно')
    except MyOwnErr:
        continue
    except ValueError:
        print(f'Вы ввели не число')
    else:
        print(f'{a}/{b} = {a/b}')
        break
