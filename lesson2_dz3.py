# l2.dz3

mes = 1
while 12 < mes or mes <= 1:
    mes = int(input('Введите номер месяца от 1 до 12: '))
# решение через list
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if mes in winter:
    print(f'{mes}-й месяц - это время года: зима')
elif mes in spring:
    print(f'{mes}-й месяц - это время года: весна')
elif mes in summer:
    print(f'{mes}-й месяц - это время года: лето')
else:
    print(f'{mes}-й месяц - это время года: осень')

# решение через dict (использовал внутри словаря кортежи, вместо списков)
year = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for i in year:
    if mes in year.get(i):
        print(f'{mes}-й месяц - это время года: {i}')
