# l3dz5

def my_func1():  # функция ввода строки и преобразования в список
    return input('Введите строку чисел разделенную пробелами, q - выход из программы\n').split()


def my_func2(my_list):  # функция подсчета суммы чисел списка до специального символа q
    list_sum = 0
    for el in my_list:
        if el == 'q':
            break
        elif el.isdigit():
            list_sum += float(el)
    return list_sum


common_sum = 0
while True:
    string = my_func1()
    string_sum = my_func2(string)
    common_sum += string_sum
    print(f'сумма строки: {string_sum}, общая сумма: {common_sum}')
    if 'q' in string:
        break
