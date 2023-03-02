from prettytable import PrettyTable
from colorama import init, Fore, Back

init(autoreset=True)

class ViewConsole:
    def show_toys_in_shop(self, data):
        mytable = PrettyTable()
        # имена полей таблицы
        mytable.field_names = ["ID", "Название игрушки", "Количество", "Частота выпадения"]
        # добавление данных по одной строке за раз
        if len(data) == 0:
            print("В базе нет игрушек")
        else:
            for row in data:
                mytable.add_row([row[0], row[1], row[2], row[3]])

        print(mytable)

    def input_console(self,text):
        input_text = input(Fore.CYAN + text)
        return input_text

    def output_console(self, text, flag):
        if flag:
            print(Back.GREEN + Fore.BLACK + text)
        else:
            print(Back.RED + Fore.BLACK + text)







