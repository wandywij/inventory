
from cashier.module.discount import Discount

def test_discount():
    test_discount = Discount(10000, 15)
    assert(test_discount.amount == 10000)