path = '1C.txt'

import datetime
import shutil 

def read_db(path):
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
    source = my_list[0].strip()

    for i in range(1, len(my_list)):
        try:
            now = datetime.datetime.now()
            path1 = my_list[i].strip()
            dist = f'\\\{path1}\C$\ProgramData\\1C\\1CEStart'
            shutil.copy2(source, dist)
            with open('log.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{now}  {path1}    OK\n')
        except:
            now = datetime.datetime.now()
            with open('logError.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{path1}\n')    
            
read_db(path)    