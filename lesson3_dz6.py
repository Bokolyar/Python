# l3dz5

def int_func(string):
    temp_list = string.split()
    # удалим из списка слова, содержащие не только латинские буквы в нижнем регистре
    for word in temp_list[:]:
        for letter in range(len(word)):
            if ord(word[letter]) < 97 or ord(word[letter]) > 122:
                temp_list.remove(word)
                break
    # преобразуем и вернем слова в тексте в слова с заглавной буквы
    return " ".join(temp_list).title()


print(int_func(input('Введите несколько слов через пробел\n')))
