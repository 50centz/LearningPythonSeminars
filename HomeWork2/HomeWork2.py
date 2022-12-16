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

number = int(input('Input a number: '))

my_list = []

for i in range(1, number + 1):
    my_list.append(round(((1 + 1 / i) ** i), 2))

sum = 0
for i in my_list:
    sum += i

print(*my_list)
print(sum)





# print(random.randint(0, 100))