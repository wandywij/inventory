import sys
 
sys.path.append("..")
# print(sys)
import unittest
from cashier.module.item import Item
from cashier.module.cart import Cart
from cashier.module.discount_tier import DiscountTier






# class TestCart(unittest.TestCase):

#     def test_sum(self):
#         calculation = Calculations(8, 2)
#         self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')



#     def test__add_cart_items():
#         cart_items = Cart()
        
#         new_item_to_be_added = Item(item_name= "Teh Kotak", qty= 2, price= 3500)
#         cart_items.add_item(new_item_to_be_added)

#         assert(len(cart_items.items) == 1)
#         assert(cart_items.items[0].item_name == "Teh Kotak")

#         new_item_to_be_added = Item(item_name= "Cheetos", qty= 3, price= 1700)
#         cart_items.add_item(new_item_to_be_added)
#         assert(len(cart_items.items) == 2)
#         assert(cart_items.items[0].item_name == "Teh Kotak")
#         assert(cart_items.items[1].item_name == "Cheetos")


#     def test_clear_cart_items():
#         cart_items = Cart()
        
#         new_item_to_be_added = Item(item_name= "Teh Kotak", qty= 2, price= 3500)
#         cart_items.add_item(new_item_to_be_added)
#         new_item_to_be_added = Item(item_name= "Cheetos", qty= 3, price= 1700)
#         cart_items.add_item(new_item_to_be_added)
#         cart_items.reset_transaction()
#         assert(len(cart_items.items) == 0)


class TestCart(unittest.TestCase):
    def test_sum(self):
        calculation = 8+2
        self.assertEqual(calculation, 10, 'The sum is wrong.')

    def test_add_cart_items(self):
        cart_items = Cart()
        
        new_item_to_be_added = Item(item_name= "Teh Kotak   ", qty= 2, price= 3500)
        cart_items.add_item(new_item_to_be_added)

        self.assertTrue(len(cart_items.items) == 1)
        self.assertTrue(cart_items.items.get("TEH KOTAK").item_name == "Teh Kotak")

        new_item_to_be_added = Item(item_name= "CheEtos  ", qty= 3, price= 1700)
        cart_items.add_item(new_item_to_be_added)
        self.assertTrue(len(cart_items.items) == 2)
        self.assertTrue(cart_items.items.get("CHEETOS").item_name == "CheEtos")
        self.assertTrue(cart_items.items.get("TEH KOTAK").item_name == "Teh Kotak")

    def test_remove_item(self):
        cart_items = Cart()
        
        new_item_to_be_added = Item(item_name= "Teh Kotak   ", qty= 2, price= 3500)
        cart_items.add_item(new_item_to_be_added)
        new_item_to_be_added = Item(item_name= "CheEtos  ", qty= 3, price= 1700)
        cart_items.add_item(new_item_to_be_added)
        new_item_to_be_added = Item(item_name= "gogo", qty= 3, price= 1700)
        cart_items.add_item(new_item_to_be_added)

        cart_items.remove_items("Teh KoTAk    ")
        self.assertTrue(cart_items.items.get("TEH KOTAK") == None)



if __name__ == '__main__':
    unittest.main()