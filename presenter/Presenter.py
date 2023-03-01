from view.ViewConsole import ViewConsole
from model.Shop import Shop
from model.Menu import Menu
class Presenter:
    def run(self):
        # my_shop = Shop()

        while True:
            menu_item = Menu().show_menu()
            match menu_item:
                case 0:
                    break
                case 1:
                    print(f"В магазине {Shop().name}\n"
                          f"Есть слудующие игрушки: ")
                    ViewConsole().show_toys_in_shop(Shop().list_toy)

                # case 2:



                # case 2:
                #     CRUD.create_note(check.check_new_note())
                # case 3:
                #     CRUD.view_ch_del()
                # case 4:
                #     exp_imp.export()
                # case 5:
                #     exp_imp.import_file()


