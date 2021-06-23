# dz5

print(f'Отчет по прибыли фирмы')
viruchka = int(input('Введите значение выручки фирмы: '))
izdergki = int(input('Введите значение издержек фирмы: '))
if viruchka > izdergki:
    print(f'Фирма приносит прибыль')
    rentab = (viruchka - izdergki)/viruchka
    print(f'Рентабельность: {rentab:.1%}')
    chisl = int(input('Какая численность вашей фирмы: '))
    result = (viruchka-izdergki)/chisl
    print(f'Выручка фирмы в соотношении на 1 человека составила: {result:.1f}')
else:
    print(f'Фирма терпит убытки')
