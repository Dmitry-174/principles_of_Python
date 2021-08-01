# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.


l = []  # создание пустого списка

# заполнение списка различными типами данных
l.append(3)
l.append(3.14)
l.append('string')
l.append([3, 3.14, 'string'])
l.append({'integral': 3, 'float': 3.14, 'string': 'string'})
l.append((3, 3.14, 'string'))
l.append({1, 3, 3, 3, 4, 5, 4})
l.append(frozenset([1, 3, 3, 3, 4, 5, 4]))
l.append(complex(3, -2))
l.append(None)
l.append(True)
l.append(b'Byte text')
l.append(bytearray(b'Byte text'))

# вывод типа данных для каждого элемента списка
for i in l:
    print(i, type(i))
