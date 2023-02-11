
try: 
    from discount_tier import DiscountTier
except:
    from cashier.module.discount_tier import DiscountTier

try:
    from item import Item
except:
    from cashier.module.item import Item

class Cart:
    items = dict()
    def __init__(self) -> None:
        pass

    def add_item(self, item: Item):
        self.items[item.item_name.strip().upper()] = Item(item_name= item.item_name.strip(), qty= item.qty, price= item.price)

    def reset_transaction(self):
        self.items.clear()

    def remove_items(self, name: str):
        self.items.pop(name.strip().upper())

    def generate_items(self):
        new_items = []
        total_price = 0
        item = Item("", 0, 0)
        i = 1
        for key in self.items.keys():
            item = self.items.get(key)
            temp = []
            temp.append(i)
            temp.append(item.item_name)
            temp.append(item.qty)
            temp.append(f"Rp {item.price}")
            amount = item.qty * item.price
            temp.append(f"Rp {amount}")
            total_price += amount
            new_items.append(temp)
            i+=1

        temp = []
        temp.append("")
        temp.append("")
        temp.append("")
        temp.append("")
        temp.append(f"\nSebelum diskon {total_price}")
        new_items.append(temp)

        temp = []
        temp.append("")
        temp.append("")
        temp.append("")
        temp.append("")
        temp.append(f"Setelah diskon {DiscountTier().getTotalPrice(amount= total_price)}")
        new_items.append(temp)
        
        return new_items
