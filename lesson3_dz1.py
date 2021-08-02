# l3dz1

def division(num1, num2):
    try:
        div = num1 / num2
        return div
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'


print('Программа выполняет деление 2-х чисел')
number1 = int(input("Введите 1-е число: "))
number2 = int(input("Введите 2-е число: "))

# вариант 1
print(f'{number1}/{number2} = {division(number1, number2)}')

# вариант 2, с использованием лямбда функции и тернарного оператора
print(f'{number1}/{number2} = '
      f'{(lambda num1,num2: num1 / num2 if num2 !=0 else "Ошибка: деление на ноль")(number1, number2)}')
