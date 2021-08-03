# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию
# int_func().

def int_func(string):
    """ Возвращает исходную строку с заглавной буквы """
    return string.title()


user_words = input("Введите строку из слов, разделенных пробелом: ").split()  # формирование списка слов из строки
for i in user_words:  # перебор слов
    print(int_func(i), end=' ')  # Вывод измененной строки
