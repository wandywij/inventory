from src import item
from src import cart

def test__add_cart_items():
    cart_items = cart.Cart()
    
    new_item_to_be_added = item.Item(item_name= "Teh Kotak", qty= 2, price= 3500)
    cart_items.add_item(new_item_to_be_added)

    assert(len(cart_items.items) == 1)
    assert(cart_items.items[0].item_name == "Teh Kotak")

    new_item_to_be_added = item.Item(item_name= "Cheetos", qty= 3, price= 1700)
    cart_items.add_item(new_item_to_be_added)
    assert(len(cart_items.items) == 2)
    assert(cart_items.items[0].item_name == "Teh Kotak")
    assert(cart_items.items[1].item_name == "Cheetos")


def test_clear_cart_items():
    cart_items = cart.Cart()
    
    new_item_to_be_added = item.Item(item_name= "Teh Kotak", qty= 2, price= 3500)
    cart_items.add_item(new_item_to_be_added)
    new_item_to_be_added = item.Item(item_name= "Cheetos", qty= 3, price= 1700)
    cart_items.add_item(new_item_to_be_added)
    cart_items.reset_transaction()
    assert(len(cart_items.items) == 0)