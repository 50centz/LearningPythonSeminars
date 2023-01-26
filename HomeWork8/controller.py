import model
import view


def input_handler(inp):
    match inp:
        case 1:
            model.choice_class()
            view.choice_object()
            model.read_db_object(model.choiceClass, view.choiceObject)
            view.print_the_magazine(model.db_list)
            model.board(view.choiceObject)
            model.save_file()
        case 2:
            model.choice_class()
            model.read_db(model.choiceClass)
            view.print_the_magazine(model.db_list)
        case 3:
            view.exit_program()

    




def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp) 