# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# формирование словаря из файла, где ключ - название предмета, значение - список занятий по предмету
with open('lesson5_task6_text.txt', 'r', encoding='utf-8') as txt:
    dict_of_subjects = {line.strip().split(':')[0]: line.strip().split(':')[1].split() for line in txt}


def num_from_string(string):
    """ Возвращает число с начала строки до первого не числового символа. Если чисел нет, то возвращает 0"""
    result = ''
    for i in string:
        if i.isdigit():
            result += i
        else:
            break
    if result != '':
        return int(result)
    else:
        return 0


for subject, content in dict_of_subjects.items():  # перебор словаря
    current_subject = 0  # начальное значение для суммы занятий текущего предмета
    for i in content:  # перебор элементов в списке для текущего значения словаря
        current_subject += num_from_string(i)  # прибавление числа занятий к сумме занятий текущего предмета
    dict_of_subjects[subject] = current_subject  # присвоение нового значения числа занятий текущего предмета

print(dict_of_subjects)
