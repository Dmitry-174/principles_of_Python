# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = 0  # начальное значение для порядкового номера месяца

# запрос порядкового номера месяца у пользователя с проверкой номера от 1 до 12
while month not in range(1, 13):
    month = int(input("Введите порядковый номер месяца: "))
    if month not in range(1, 13):
        print("Порядковый номер месяца должен быть от 1 до 12")

# решение через list
list_of_seasons = ["зима", "весна", "лето", "осень"]
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
# осень - остальное, валидация введеного номера проведена

if month in winter:
    print(list_of_seasons[0])
elif month in spring:
    print(list_of_seasons[1])
elif month in summer:
    print(list_of_seasons[2])
else:
    print(list_of_seasons[3])

# решение через dict
dict_of_seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for season, months in dict_of_seasons.items():
    if month in months:
        print(season)
