import model
import view


def input_handler(inp):
    match inp:
        case 2:
            view.exit_program()

    




def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp) 