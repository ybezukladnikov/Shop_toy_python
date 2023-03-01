from model.ReadWriteBD import ReadWriteBD


class Shop:
    name = "Детский мир"
    list_toy = []

    def __init__(self):
        self.list_toy = ReadWriteBD().read_bd()



