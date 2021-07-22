class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []
while True:
    b = input('Введите число (q - окончание ввода): ')
    if b == 'q':
        break
    try:
        if not b.isdigit():
            raise MyOwnErr('Вы ввели не число')
        else:
            a.append(b)
            print(a)
    except MyOwnErr as err:
        print(err)

print(f'итоговый список: {a}')
