
def main_menu():
    menu_list = [
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'   
    ]
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи цифру: '))
    return user_input

def show_all(db):
    for i in range(len(db)):
        user_id = i + 1
        print(user_id, end=' ')
        for v in db[i].values():
            print(f'{v}', end=' ')
        print()    
        


