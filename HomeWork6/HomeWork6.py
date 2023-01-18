# лямбд, filter, map, zip, enumerate, list comprehension

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


