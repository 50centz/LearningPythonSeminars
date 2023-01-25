import model
import view


def input_handler(inp):
    match inp:
        case 1:
            view.choice_class()
            view.choice_object()
            model.read_db_object(view.choiceClass, view.choiceObject)
            view.print_the_magazine(model.db_list)
        case 3:
            view.choice_class()
            model.read_db(view.choiceClass)
            view.print_the_magazine(model.db_list)
        case 4:
            view.exit_program()

    




def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp) 