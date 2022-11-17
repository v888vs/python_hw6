# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить
# нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете
# вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

# def srch_symb(s):
#     if s[0] in '+-':
#         return s[0]
#
# l1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# ins_el = '"'
# l2 = []
# i = 0
# while i < len(l1):
#     num = srch_symb(l1[i])
#     if l1[i].isdigit() == True or  (num and l1[i][1:].isdigit()) or (num and l1[i].isdigit()): #для чисел со знаками
#         if len(l1[i]) < 2 :
#             l1[i] = l1[i].zfill(2)
#         elif num:
#             l1[i] = num + l1[i][1:].zfill(2)
#         l2.append(l1[i]) #Для вывода только чисел
#         l1.insert(i, ins_el)
#         l1.insert(i + 2, ins_el)
#         i += 3
#     else:
#         i += 1
# print(l1, '\n')
# l1 = ' '.join(l1)
# print(l1, '\n')
# print(l2) #Вывод только чисел


# * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран
# фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из
# элементов списка, как привести их к корректному виду. Можно ли при
# этом не создавать новый список?

# l1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for i in l1:
#     name = i.split()[-1].capitalize()
#     print(f'Привет, {name} !')


# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены
# этих товаров по возрастанию, написав минимум кода?

# import random
# import math
#
# def create_price():
#  rand_price = [round(random.uniform(0, 99.99), 2) for i in range(0, 10)]
#  return(rand_price)
#
# def print_price(l1):
#     for i in l1:
#         rr = math.trunc(i)
#         cns = int(round((i % 1) * 100, 2))
#         if (rr < 10 and cns < 10):
#             print(f'0{rr} руб 0{cns} коп')
#         elif (rr > 10 and cns < 10):
#             print(f'{rr} руб 0{cns} коп')
#         elif (rr < 10 and cns > 10):
#             print(f'0{rr} руб {cns} коп')
#         else:
#             print(f'{rr} руб {cns} коп')
#
# l1 = create_price()
# print(l1)
# print(l1.sort())    # Для сортировки на возрастание
# l2 = l1[::-1]       # Новый список на убывание
# print(l2)           #
# print_price(l1)
# max1 = l1[-5:]      # Для вывода максимальных 5 цен, по возрастанию
# print(max1)         #
# print_price(max1)   #