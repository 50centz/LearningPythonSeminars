
def main_menu():
    menu_list = [
                    'Показать все контакты',
                    'Открыть телефонную книгу',
                    'Сохранить телефонную книгу',
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
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()
    print(' ')            



def db_success(db):
    if db:
        print(' ')
        print('Телефонная книга открыта')
        print(' ')
        return True
    else:
        print(' ')
        print('Телефонная книга пуста или не открыта')
        print(' ')
        return False



def save_file(db):
    if db_success(db):
        with open('database.txt', 'w') as data:
            data.write('')

        for i in range(len(db)):
            for j in db[i].values():
                data = str(j)
                with open('database.txt', 'a', encoding='UTF-8') as file:
                    file.write(f'{data};')
            with open('database.txt', 'a', encoding='UTF-8') as file:
                    file.write(f'\n')          
               

def create_contact():
    
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\t Введите фамилию: ')
    new_contact['firstname'] = input('\t Введите имя: ')
    new_contact['phone'] = input('\t Введите телефон: ')
    new_contact['comment'] = input('\t Введите комментарий: ')
    print(' ')
    print('Не забудьте сохранить телефонную книгу !!!!!!!!!!!!!!!!!!!!\n')
    return new_contact    


def change_contact(db):
    if db_success(db):
        choice = int(input(f'Выберите номер контакта: '))
        my_dict = dict()
        my_dict['lastname'] = input('\t Введите фамилию: ')
        my_dict['firstname'] = input('\t Введите имя: ')
        my_dict['phone'] = input('\t Введите телефон: ')
        my_dict['comment'] = input('\t Введите комментарий: ')
        db[choice - 1] = my_dict
        print(' ')
        print('Не забудьте сохранить телефонную книгу !!!!!!!!!!!!!!!!!!!!!!!')
        print(' ')

def delete_contact(db):
    if db_success(db):
        choice = int(input(f'Выберите номер контакта: '))

        db.pop(choice - 1)

        print(' ')
        print('Не забудьте сохранить телефонную книгу !!!!!!!!!!!!!!!!!!!!!!!')
        print(' ')



def exit_program():
    print('Завершение программы.')
    exit()

