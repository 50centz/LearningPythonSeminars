# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]


import random
import itertools

number = int(input('Enter the degree of the polynomial: '))

# if number == 0:
#     print('The degree cannot be zero, enter a number greater than zero!!! ')

def creating_a_coefficient(number):
    my_list = []
    for i in range(0, number):
        my_list.append(random.randint(-100, 100))
    while my_list[0] == 0:
        my_list[0] = random.randint(-100, 100)    
    return my_list    

def create_polynomial(number, my_list):
    my_list2 = ['*x^'] * (number - 1) + ['*x']
    my_list3 = [[a, b, c] for a, b, c in itertools.zip_longest(my_list, my_list2, range(number, 1, -1), fillvalue = '')]
    for i in range(1, len(my_list3)):
        if my_list[i] < 0:
            my_list3[i][0] = my_list3[i][0] * -1
            my_list3[i].insert(0, ' - ')
        elif my_list[i] > 0:
            my_list3[i].insert(0, ' + ')           
    my_list3 = list(itertools.chain(*my_list3))  
    my_list3[-1] = ' = 0'
    return "".join(map(str, my_list3)).replace(' 1*x',' x')


def sum_of_the_polynomial(mylist1, mylist3):
    my_list4 = []
    for i in range(0, len(my_list)):
        my_list4.append(my_list[i] + my_list2[i])
    return my_list4    

       


my_list = creating_a_coefficient(number)
# print(my_list)
pol1 = create_polynomial(number, my_list)
# print(pol1)

my_list2 = creating_a_coefficient(number)
# print(my_list2)
pol2 = create_polynomial(number, my_list2)
# print(pol2)

my_list3 = sum_of_the_polynomial(my_list, my_list2)
# print(my_list3)
pol3 = create_polynomial(number, my_list3)
# print(pol3)


with open('file1.txt', 'w') as data:
    data.write(pol1)

with open('file2.txt', 'w') as data:
    data.write(pol2)    

with open('Sum_of_the_polynomial.txt', 'w') as data:
    data.write(pol3)    