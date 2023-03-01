from model.ReadWriteBD import ReadWriteBD


class Shop:
    name = "Shop Toys"

    def __init__(self):
        self.list_toy = ReadWriteBD().read_bd()



