class Item:
    def __init__(self, item_name: str, qty: int, price: int) -> None:
        self.item_name = item_name
        self.price = price
        self.qty = qty