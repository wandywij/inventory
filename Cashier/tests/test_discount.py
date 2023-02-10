from src import discount

def test_discount():
    test_discount = discount.Discount(10000, 15)
    assert(test_discount.amount == 10000)