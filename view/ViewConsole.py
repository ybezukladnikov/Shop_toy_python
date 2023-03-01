from prettytable import PrettyTable

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



