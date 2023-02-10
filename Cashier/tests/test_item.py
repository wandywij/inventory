from src import item


def test_item():

    test_item = item.Item(item_name= "Biskuit Oreo", qty = 3, price= 10000)
    assert(test_item.item_name == "Biskuit Oreo")
    assert(test_item.qty == 3)
    assert(test_item.price == 10000)
