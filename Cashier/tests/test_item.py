from src import item

test_item = item.Item(name: "Biskuit Oreo", qty: 3, price: 10000)

def test_item():
    assert(test_item.name == "Biskuit Oreo")
    assert(test_item.qty == 3)
    assert(test_item.name == 10000)
