from model.ReadWriteBD import ReadWriteBD
from model.Check import Check
from view.ViewConsole import ViewConsole
import datetime


class Shop:

    name = "Детский мир"
    list_toy = []
    list_for_issue = []
    ReadWriteBD = ReadWriteBD()
    view = ViewConsole()

    # def __init__(self):
    #     self.list_toy = self.ReadWriteBD.read_bd()

    def add_toy_inDB(self):
        new_toy = []
        name = Check().check_name_toy()
        amount_toy = Check().check_amount_toy()
        frequency = Check().check_frequency_toy()
        for i in (name, amount_toy, frequency):
            new_toy.append(i)

        self.ReadWriteBD.write_bd(f"INSERT INTO `toys_in_shop` (title_toy, amount, frequency) "
                                    f"VALUES ('{new_toy[0]}', '{new_toy[1]}', '{new_toy[2]}');")

        self.view.output_console("Игрушка успешно добавлена в базу", True)

    def get_list_toy(self):
        self.list_toy = self.ReadWriteBD.read_bd("SELECT * FROM `toys_in_shop`")

    def get_list_for_issue(self):
        self.list_for_issue = self.ReadWriteBD.read_bd("SELECT id, title_toy, date_of_winning "
                                                       "FROM `toys_for_delivery`"
                                                       "WHERE toy_issued = 0")

    def give_toy(self):
        self.get_list_for_issue()
        if not len(self.list_for_issue) ==0:
            id_for_give = self.list_for_issue[0]['id']
            self.ReadWriteBD.write_bd(f"UPDATE `toys_for_delivery` "
                                      f"SET toy_issued = '1',"
                                      f"date_issue = '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}'"
                                      f"WHERE id = '{id_for_give}';")
            self.view.output_console("Игрушка успешно выдана", True)
        else:
            self.view.output_console('Нет игрушек для выдачи', False)













