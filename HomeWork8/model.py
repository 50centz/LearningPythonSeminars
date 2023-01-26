db_list = []



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

