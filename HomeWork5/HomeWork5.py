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


