import random

# from random import randint
# randint(a, b)
# from random import randint as RI
# Ri(a, b)


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# number = float(input('Input a number: '))
# number = str(number)
# number = list(number)

# my_list = []

# for item in number:
#     my_list.append(item.replace('.', '0'))

# result = list(map(int, my_list))

# total = 0

# for i in result:
#     total += i

# print(total)





# Второе решение первой задачи




# number = float(input('Input a number: '))

# number = str(number)

# sum = 0

# for i in number:
#     if i.isdigit():
#         sum += int(i)

# print(sum)        





###########################################################################################################################






# 2. Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# number = int(input('Input a number: '))

# my_list = []

# for i in range(1, number + 1):
#     my_list.append(round(((1 + 1 / i) ** i), 2))

# sum = 0
# for i in my_list:
#     sum += i

# print(*my_list)
# print(sum)




###############################################################################################################################


# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int


# print(random.randint(0, 100))

my_list = []

for i in range(1, random.randint(3, 100)):
    my_list.append(random.randint(0, 100))

print(my_list)

# 1 способ

my_list2 = my_list.copy()

my_list2 = list(map(str, my_list))

my_list2.reverse()

print(*my_list2)

# 2 способ

my_list3 = my_list.copy()

for i in range(len(my_list3) - 1):
    if my_list3[i] > my_list3[i + 1]:
        temp = my_list3[i]
        my_list3[i] = my_list3[i + 1]
        my_list3[i + 1] = temp

print(my_list3)
# print(my_list3.index(i))

# 3 способ 

my_list4 = my_list.copy()

for i in my_list4:
    element = my_list4.pop(random.randint(1, len(my_list4)- 2))
    my_list4.insert(random.randint(1, len(my_list4) - 1), element)

print(my_list)
print(my_list4)    