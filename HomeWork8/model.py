db_list = []

path = '7B.txt'

def read_db(path):
    global db_list
    my_object_dict = dict()
    my_ocenka = dict()

    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
    for i in my_list:
        my_object = i.strip().split(';')[0]
        temp = i.strip().split(';')[1]
        temp1 = temp.strip().split(',')
        for j in temp1:
            name = j.strip().split(':')[0]
            ocenka = list(map(int, j.strip().split(':')[1].strip().split(' ')))
            my_ocenka[name] = [ocenka]
        my_object_dict[my_object] = (my_ocenka)    
    db_list.append(my_object_dict)        

   
        
read_db(path) 
a = len(db_list)


for i in range(len(db_list)):
    print(db_list[i])


            


            
            
            





