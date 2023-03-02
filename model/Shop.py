from model.ReadWriteBD import ReadWriteBD
from model.Check import Check
from view.ViewConsole import ViewConsole


class Shop:

    name = "Детский мир"
    list_toy = []
    ReadWriteBD = ReadWriteBD()
    view = ViewConsole()

    def __init__(self):
        self.list_toy = self.ReadWriteBD.read_bd()

    def add_toy_inDB(self):
        new_toy = []
        name = Check().check_name_toy()
        amount_toy = Check().check_amount_toy()
        frequency = Check().check_frequency_toy()
        for i in (name, amount_toy, frequency):
            new_toy.append(i)

        self.ReadWriteBD.write_bd(new_toy)
        self.view.output_console("Игрушка успешно добавлена в базу", True)








