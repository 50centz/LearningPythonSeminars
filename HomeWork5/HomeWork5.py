import pygame
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


# pygame.init()

# def drawGrid(scr):
#     pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
#     pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
#     pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
#     pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

# def drawTicTac(scr, items):
#     for i in range(3):
#         for j in range(3):
#             if items[i][j] == '0':
#                 pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
#             elif items[i][j] == 'x':
#                 pygame.draw.line(scr, (0, 0 , 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
#                 pygame.draw.line(scr, (0, 0 , 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)


# def winCheck(fi, symbol):
#     flagWin = False
#     for line in fi:
#         if line.count(symbol) == 3:
#             flagWin = True

#     for i in range(3):
#         if fi[0][i] == fi[1][i] == fi[2][i] == symbol:
#             flagWin = True

#     if fi[0][0] == fi[1][1] == fi[2][2] == symbol:
#         flagWin = True

#     if fi[0][2] == fi[1][1] == fi[2][0] == symbol:
#         flagWin = True

#     return flagWin    






# windowSize = (300, 300)

# window = pygame.display.set_mode(windowSize)
# screen = pygame.Surface(windowSize)

# pygame.display.set_caption('Крестики-нолики')
# screen.fill((255, 255, 255))

# field = [['', '', ''],
#          ['', '', ''],
#          ['', '', '']]

# mainloop = True
# game_over = False

# while mainloop:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             mainloop = False

#         if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             pos = pygame.mouse.get_pos()
#             if field[pos[1] // 100][pos[0] // 100] == '':
#                 field[pos[1] // 100][pos[0] // 100] = 'x'
#                 x, y = random.randint(0, 2), random.randint(0, 2)
#                 while field[x][y] != '':
#                     x, y = random.randint(0, 2), random.randint(0, 2)
#                 field[x][y] = '0'

#             playerWin = winCheck(field, 'x')
#             botWin = winCheck(field, '0')
#             if playerWin or botWin:
#                 game_over = True
#                 if playerWin:
#                     pygame.display.set_caption('Winner man')
#                 else:
#                     pygame.display.set_caption('Winner bot')
#             elif field[0].count('x') + field[0].count('0') + field[1].count('x') + field[1].count('0') + field[2].count('x') + field[2].count('0') == 8:
#                 game_over = True
#                 pygame.display.set_caption('Ничья')                  

            
#     drawTicTac(screen, field)      
#     drawGrid(screen)
#     window.blit(screen, (0, 0))
#     pygame.display.update()      


#########################################################################################################################################################################


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def dataRrecording(data):
    with open('recording.txt', 'w') as recording:
        recording.write(data)


def readData():
    rec = open('recording.txt', 'r')
    data = rec.read()
    rec.close
    return data

def dataCompression(data):
    res = []
    count = 1
    data = list(data)
    data.append('/?')
    
    for i in range(1,len(data) - 1):
        count +=1
        if data[i] != data[i + 1]:
            res.append(str(count) + data[i])
            count = 0
    res = ''.join(res)        
    return res        

def dataRecovery(data):
    res = []
    data = list(data)
    for i in range(0, len(data), 2):
        res.append(int(data[i]) * data[i + 1])
    res = ''.join(res)
    return res



stroka = 'aaccddfftt'

result = dataCompression(stroka)
dataRrecording((result))
recovery = readData()
print(dataRecovery(recovery))
