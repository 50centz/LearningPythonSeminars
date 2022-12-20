import random

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



# a = int(input('Enter the size of the list: '))

# my_list = []

# for i in range(0, a):
#     my_list.append(random.randint(0, 100))

# print(*my_list)

# sum = 0

# for i in my_list[1::2]:
#     sum += i
    
# print(sum)




####################################################################################################################################



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# a = int(input('Enter the size of the list: '))

# my_list = []

# for i in range(0, a):
#     my_list.append(random.randint(0, 10))

# print(my_list)

# my_list2 = []

# size = 0

# if len(my_list) % 2 == 0:
#     size = int(len(my_list) / 2)
# else:
#     size = int(len(my_list) / 2 + 1)

# print(size)

# b = -1

# for i in range(0, size):
#     my_list2.append(my_list[i] * my_list[b])
#     b = -1 + b
    
# print(my_list2)   

####################################################################################################################################


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



# index = random.randint(0, 3)    Переменная для округления вещественного числа 
# my_list.append(random.uniform(0,10), index))  Получаем вещественные числа, рандомно

# size = int(input('Enter the size of the list: '))

# my_list = []

# for i in range(0, size):
#     my_list.append(round(random.uniform(0, 10), 2))

# print(my_list)

# my_list2 = []

# for i in my_list:
#     my_list2.append(round(i % 1, 2))

# print(my_list2)

# max = 0.01
# min = 100000

# for i in my_list2:
#     if max < i:
#         max = i
#     elif min > i:
#         min = i
        

# print(max)
# print(min)        

# if min == 0:
#     print('The fractional part is zero, the calculation is not performed')
# else:
#     print(max - min)    


######################################################################################################################################################

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Input a number: '))

# my_list = []

# while number > 0:
#     my_list.append(number % 2)
#     number = int(number / 2)
#     print(number)

# print(*my_list)
# my_list2 = my_list.copy()
# my_list2.reverse()
# print(*my_list2)


##########################################################################################################################################################


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

    




