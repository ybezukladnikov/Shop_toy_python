from view.ViewConsole import ViewConsole
from model.Shop import Shop
# from model.Menu import Menu
from model.Check import Check
class Presenter:
    view = ViewConsole()
    def run(self):
        while True:
            self.view.output_console(f"Магазин игрушек {Shop().name}",True)
            ViewConsole().show_main_menu()
            menu_item = Check().check_main_menu()
            match menu_item:
                case 0:
                    break
                case 1:
                    ViewConsole().show_toys_in_shop(Shop().list_toy)
                case 2:
                    Shop().add_toy_inDB()



                # case 2:
                #     CRUD.create_note(check.check_new_note())
                # case 3:
                #     CRUD.view_ch_del()
                # case 4:
                #     exp_imp.export()
                # case 5:
                #     exp_imp.import_file()


