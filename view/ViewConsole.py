from prettytable import PrettyTable

class ViewConsole:
    def show_toys_in_shop(self, data):
        mytable = PrettyTable()
        # имена полей таблицы
        mytable.field_names = ["ID", "Имя заметки", "Краткое содержание заметки", "Дата создания",
                               "Дата последнего изменения"]
        # добавление данных по одной строке за раз
        for row in data:
            mytable.add_row([row[0], row[1], row[2], row[3]])

        # вывод таблицы в терминал
        print(mytable)

