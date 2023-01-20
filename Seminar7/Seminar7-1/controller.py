import model
import view

model.read_db('database.txt')

# print(temp)

user_choise = view.main_menu()

def input_handler(inp):
    match inp:
        case 1:
            view.show_all(model.db_list)
        


input_handler(user_choise)            

