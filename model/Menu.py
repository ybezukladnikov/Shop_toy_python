from model.Check import Check
class Menu:
    MENU_ITEMS = {
        1: "Показать игрушки в базе",
        2: "Добавить игрушку в базу",
        0: "Выход"
    }
    def show_menu(self):
        print('Магазин игрушек')
        for operNum, operDesc in self.MENU_ITEMS.items():
            print(f"{operNum}. {operDesc}")

        return Check().check_main_menu()
