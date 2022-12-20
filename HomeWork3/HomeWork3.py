import random

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



# a = int(input('Enter the size of the list: '))

# Заполняем список рандомными числами, размер списка вводит пользователь

# my_list = []

# for i in range(0, a + 1):
#     my_list.append(random.randint(0, 100))

# print(*my_list)

# Суммируем элементы на нечётных позициях     

# sum = 0

# for i in my_list[1::2]:
#     sum += i
    
# print(sum)




####################################################################################################################################



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



a = int(input('Enter the size of the list: '))

# Заполняем список рандомными числами, размер списка вводит пользователь

my_list = []

for i in range(0, a):
    my_list.append(random.randint(0, 10))

print(my_list)

my_list2 = []

size = 0
if len(my_list) % 2 == 0:
    size = int(len(my_list) / 2)
else:
    size = int(len(my_list) / 2 + 1)

print(size)        
b = -1

for i in range(0, size):
    my_list2.append(my_list[i] * my_list[b])
    b = -1 + b
    

print(my_list2)   





# index = random.randint(0, 3)
# my_list.append(random.uniform(0,10), index))