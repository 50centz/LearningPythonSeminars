# лямбд, filter, map, zip, enumerate, list comprehension
from random import randint as RA
import random

# Написать строчный калькулятор 

# stroka = '5+4*7+6*8*7+4/9'
# stroka = list(stroka)

# def umn(my_list):
#     start = True
#     stroka = my_list
#     while start:
#         start = False
#         for i in range(len(stroka)):
#             if stroka[i] == '*' or stroka[i] == '/':
#                 index = i
#                 ari = stroka[i]
#                 if ari == '*':
#                     result = int(stroka[i-1]) * int(stroka[i + 1])
#                     stroka[i - 1] = result
#                     stroka.pop(index)
#                     stroka.pop(index)
#                     start = True
#                     break
#                 elif ari == '/':
#                     result = int(stroka[i-1]) / int(stroka[i + 1])
#                     stroka[i - 1] = result
#                     stroka.pop(index)
#                     stroka.pop(index)
#                     start = True
#                     break
#     return stroka            

    
# def sum(my_list):
#     stroka = my_list
#     start = True
#     while start:
#         start = False
#         for i in range(len(stroka)):
#             if stroka[i] == '+' or stroka[i] == '-':
#                 index = i
#                 ari = stroka[i]
#                 if ari == '+':
#                     result = int(stroka[i-1]) + int(stroka[i + 1])
#                     stroka[i - 1] = result
#                     stroka.pop(index)
#                     stroka.pop(index)
#                     start = True
#                     break
#                 elif ari == '-':
#                     result = int(stroka[i-1]) - int(stroka[i + 1])
#                     stroka[i - 1] = result
#                     stroka.pop(index)
#                     stroka.pop(index)
#                     start = True
#                     break
#     return stroka            
        

              
    

# def fun(my_list):
#     while '*' in my_list or '/' in my_list:
#         for i in range(len(my_list)):
#             if my_list[i] == '*':
#                 umn(my_list)
#                 break
#             elif my_list[i] == '/':
#                 umn(my_list)
#                 break

#     while '+' in my_list or '-' in my_list:
#         for i in range(len(my_list)):
#             if my_list[i] == '+':
#                 sum(my_list)
#                 break
#             elif my_list[i] == '-':
#                 sum(my_list)
#                 break
#     return my_list                


# print(*fun(stroka))            

        

#################################################################################################################################################################################


# Сократить первые задания 
# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

# БЫЛО 

# my_list = []
# for i in range(1, random.randint(3, 100)):
#     my_list.append(random.randint(0, 100))
# print(my_list)


# СТАЛО

# my_list = [RA(0, 100) for i in range(RA(3, 100))]
# print(my_list)



# 2. Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# БЫЛО 

# number = int(input('Input a number: '))

# my_list = []

# for i in range(1, number + 1):
#     my_list.append(round(((1 + 1 / i) ** i), 2))

# sum = 0
# for i in my_list:
#     sum += i

# print(*my_list)
# print(sum)

# СТАЛО

digit = int(input('Input a digit: '))
my_list = [i + 1 for i in range(digit)]
my_list = list(map(lambda x : (1 + 1/ x) ** x, my_list))
sum = 0
for i in my_list:
    sum += i
print(my_list)    
print(round(sum, 2))  
  
    
    