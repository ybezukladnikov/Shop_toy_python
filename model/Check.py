from view.ViewConsole import ViewConsole


class Check:
    my_view = ViewConsole()
    def check_main_menu(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите номер пункта, который хотите выполнить: '))
                if 0 <= num <= 6:
                    break
                else:
                    self.my_view.output_console('Такого пункта меню нет! Попробуйте снова.', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num

    def check_name_toy(self):
        while True:
            name = self.my_view.input_console('Введите название игрушки (до 15 символов): ')
            if len(name)>15 or len(name)==0:
                self.my_view.output_console('Неверная длина названия', False)
                continue
            break
        return name

    def check_amount_toy(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите количество игрушек: '))
                if num > 0:
                    break
                else:
                    self.my_view.output_console('Число не может быть отрицательным', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num

    def check_frequency_toy(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите частоту выпадения игрушки: '))
                if 0< num < 100:
                    break
                else:
                    self.my_view.output_console('Число должно быть в диапозоне от 0 до 100', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num








