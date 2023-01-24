import model
import view


def input_handler(inp):
    match inp:
        case 3:
            model.read_db('7B.txt')
            view.print_the_magazine(model.db_list)
        case 4:
            view.exit_program()

    




def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp) 