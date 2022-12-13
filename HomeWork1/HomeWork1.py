#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# not (x or y or z ) == not x and not y and not z 


# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num = int(input('Input a number: '))

# if(num < 6 and num > 0):
#     print('Нет')
# elif(num > 5 and num < 8):
#     print('Да')
# else:
#     print('Number is incorrect !!!')    


###################################################################################################################################


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = float(input('Enter the coordinates of the X point: '))
# y = float(input('Enter the coordinates of the Y point: '))

# if(x == 0 or y == 0):
#     print('The coordinates must not be zero !!!')
# elif(x > 0 and y > 0):
#     print('1 plane')
# elif(x < 0 and y > 0):
#     print('2 plane')
# elif(x < 0 and y < 0):
#     print('3 plane')
# elif(x > 0 and y < 0):
#     print('4 plane')                


######################################################################################################################################


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


number = int(input('Enter the plane number: '))

if(number < 1 or number > 4):
    print('Invalid number !!!')
elif(number == 1):
    print('Range of possible coordinates x > 0 and y > 0')
elif(number == 2):
    print('Range of possible coordinates x < 0 and y > 0')
elif(number == 3):
    print('Range of possible coordinates x < 0 and y < 0')
elif(number == 4):
    print('Range of possible coordinates x > 0 and y < 0')            
