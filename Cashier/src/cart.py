from src import item

class Cart:
    items = list[item.Item]()
    def __init__(self) -> None:
        pass

    def addItem(self, item: item.Item):
        print(type(self.items))
        self.items.append(item)
