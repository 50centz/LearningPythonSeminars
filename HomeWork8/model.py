db_list = []
choiceClass = ''



def read_db(path):
    global db_list
    db_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
    for i in my_list:
        my_object_dict = dict()
        my_ocenka = dict()
        my_object = i.strip().split(';')[0]
        temp = i.strip().split(';')[1]
        temp1 = temp.strip().split(',')
        for j in temp1:
            name = j.strip().split(':')[0]
            ocenka = list(map(int, j.strip().split(':')[1].strip().split(' ')))
            my_ocenka[name] = [ocenka]
        my_object_dict[my_object] = (my_ocenka)    
        db_list.append(my_object_dict)        
 
        
def read_db_object(path, choice):
    global db_list
    db_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
    for i in my_list:
        my_object_dict = dict()
        my_ocenka = dict()
        my_object = i.strip().split(';')[0]
        if my_object == choice:
            temp = i.strip().split(';')[1]
            temp1 = temp.strip().split(',')
            for j in temp1:
                name = j.strip().split(':')[0]
                ocenka = list(map(int, j.strip().split(':')[1].strip().split(' ')))
                my_ocenka[name] = [ocenka]
            my_object_dict[my_object] = (my_ocenka)    
            db_list.append(my_object_dict)



def choice_class():
    global choiceClass
    choiceClass = ' '
    print('7A')
    print('7B')
    cl = input('Выберите класс: ').upper()
    while True:
        if cl == '7A' or cl == '7B':
            break
        else:
            cl = input('Введите корректный класс: ').upper()
    choiceClass = cl + '.txt'


def board(c_O):
    name = input('Кто пойдёт к доске ? ')
    while True:
        if name == 'Иванов Максим' or name == 'Петров Сергей' or name == 'Сидоров Иван' or name == 'Кузнецов Артём' or name == 'Григорьев Сергей' or name == 'Васильев Иван':
            break
        else:
            name = input('Введите корректно имя: ')
    choice = int(input('Какую оценку поставим ? '))
    for i in range(len(db_list)):
        for k in db_list[i].keys():
            if k == c_O:
                for v in db_list[i].values():
                    for j,z  in v.items():
                        if name == j:
                            z[0].append(choice)
                                                
                

def save_file():
    db_list1 = db_list.copy()
    a = ''
    for i in range(len(db_list1)):
        for k in db_list1[i].keys():
            a = k
    h = a                
    read_db(choiceClass)
    
    with open(choiceClass, 'w') as file:
        file.write('')
    for w in range(len(db_list)):
        for m in db_list[w].keys():
            if h == m:
                for q in range(len(db_list1)):
                    for e in db_list1[q].keys():
                        with open(choiceClass, 'a', encoding='UTF-8') as file:
                            file.write(f'{e};')
                        for r in db_list1[q].values():
                            for t, y in r.items():
                                y = ', '.join(map(str, y))
                                y = y.replace('[', '')
                                y = y.replace(']', '')
                                y = y.replace(',', '')
                                with open(choiceClass, 'a', encoding='UTF-8') as data:
                                    data.write(f'{t}:{y},')
                            with open(choiceClass, 'a', encoding='UTF-8') as fi:          
                                fi.write(f'\n')
                                       
            else:
                with open(choiceClass, 'a', encoding='UTF-8') as file:
                            file.write(f'{m};')                                                    
                for v in db_list[w].values():
                    for j,z  in v.items():
                        a = ' '.join(map(str, z))
                        a = a.replace('[', '')
                        a = a.replace(']', '')
                        a = a.replace(',', '')
                        with open(choiceClass, 'a', encoding='UTF-8') as data:
                            data.write(f'{j}:{a},')
                    with open(choiceClass, 'a', encoding='UTF-8') as f:        
                        f.write(f'\n')
                                    
                                    
           


    

