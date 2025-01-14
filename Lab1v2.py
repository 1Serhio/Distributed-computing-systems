import random
import time
import datetime
from statistics import mean

print("Выберите метрику: 1 - Температура, 2 - Влажность воздуха, 3 - Качество воздуха, 4 - Другое / Неизвестно")
choice = int(input())
print("Введите нижнее значение интервала")
Pmin = int(input())
print("Введите верхнее значение интервала")
Pmax = int(input())

print("Началась генерация чисел")

match choice:
    case 1:
        metrika = "Температура"
        symb = "°C"
    case 2:
        metrika = "Влажность водуха"
        symb = "%"
    case 3:
        metrika = "Качество воздуха"
        symb = "AQI"
    case _:
        metrika = ""
        symb = ""

f = open('lab1.txt', 'w')
kolvo = 5
p = 0

znach = []

while p < kolvo:
    for i in range(59):
        znach.append(random.uniform(Pmin, Pmax))
        time.sleep(0.05)
    f.write(str(datetime.datetime.now()).split('.')[0] + " " + metrika + " " + str(format(mean(znach), ".2f")) + symb + "\n")
    znach = []
    p+=1
f.close()

print("Значения сохранены в файле Lab1")