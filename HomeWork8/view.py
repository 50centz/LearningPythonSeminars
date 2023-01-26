choiceObject = ''

def main_menu():
    print(' ')
    menu_list = [
                    'Список классов',
                    'Посмотреть весь журнал',
                    'Выход из программы'   
                ]
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    print(' ')    
    user_input = int(input('Введи пункт: '))
    
    return user_input

def print_the_magazine(db):
    for i in range(len(db)):
        for k in db[i].keys():
            print(' ')
            print(k)
        for v in db[i].values():
            for j,z  in v.items():
                a = ', '.join(map(str, z))
                print(f'\t{j} {a}' )
            print(' ')  





def choice_object():
    global choiceObject
    choiceObject = ' '
    menu_list = [
                    'Список предметов',    
                    '\tМатематика',
                    '\tЛитература',
                    '\tИстория'  
                ]
    for i in range(len(menu_list)):
        print(menu_list[i])
    choiceObject = input('Выберите предмет: ').capitalize()
    while True:
        if choiceObject == 'Математика' or choiceObject == 'Литература' or choiceObject == 'История':
            break
        else:
            choiceObject = input('Введите корректное название предмета: ').capitalize()
           
       



def exit_program():
    print('Завершение программы')
    exit()
