

def main_menu():
    menu_list = [
                    'Введите класс',
                    'Выход'   
                ]
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи цифру: '))
    return user_input


def exit_program():
    print('Завершение программы')
    exit()
