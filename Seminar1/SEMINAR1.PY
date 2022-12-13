# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет





# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))
# c = int(input('Введите 3 число: '))
# d = int(input('Введите 4 число: '))
# e = int(input('Введите 5 число: '))
# max = a

my_list = []

for i in range(5):
    number = int(input('Input digit: '))
    my_list.append(number)
    # my_list.append (int(input(f'Введите {i + 1} число ')))

my_max = my_list[0]

for i in my_list:
    if my_max < i:
        my_max = i

print(my_max)    


#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# not (x or y or z ) == not x and not y and not z               