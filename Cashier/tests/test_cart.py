from src import item
from src import cart

def test_cart_items():
    cart_items = cart.Cart(list[item.Item])
    
    new_item_to_be_added = item.Item(item_name= "Teh Kotak", qty= 2, price= 3500)
    cart_items.addItem(new_item_to_be_added)

    assert(len(cart_items) == 1)
    assert(cart_items[0].item_name == "Teh Kotak")