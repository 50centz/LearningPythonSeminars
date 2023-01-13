import random
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


# candies = int(input('Enter the number of candies: '))

# oneMove = 28

# victory = candies % (oneMove + 1)

# men = 1
# bot = 0

# firstMove = random.randint(0, 1)
# print(firstMove)

# if firstMove == men:
#     candies -= victory
#     while candies > 0:
#         bot = random.randint(1, 28)
#         candies -= bot
#         if candies == 0:
#             print('Winner bot')
#         men = (oneMove + 1) - bot
#         candies -= men
#         if candies == 0:
#             print('Winner men')
# else:
#     while candies > 0:
#         bot = random.randint(1, 28)
#         candies -= bot
#         if candies <= 0:
#             print('Winner bot')
#             break
#         men = random.randint(1, 28)
#         candies -= men
#         if candies <= 0:
#             print('Winner man')
#             break


#########################################################################################################################################################################


# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


