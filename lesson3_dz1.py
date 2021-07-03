# l3dz1

def division(p_1, p_2):
    try:
        div = p_1 / p_2
        return div
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'


print('Программа выполняет деление 2-х чисел')
ch_1 = int(input("Введите 1-е число: "))
ch_2 = int(input("Введите 2-е число: "))
print(f'{ch_1}/{ch_2} = {division(ch_1, ch_2)}')

print(f'{ch_1}/{ch_2} = {(lambda p_1,p_2: p_1 / p_2 if p_2 !=0 else "Ошибка: деление на ноль")(ch_1, ch_2)}')
