
from cashier.module.discount_tier import DiscountTier
import unittest

class TestDiscountTier(unittest.TestCase):
    

    def test_discount_tier(self):
        discount_tier = DiscountTier()
        
        total_price_to_be_paid = discount_tier.getTotalPrice(200000)
        self.assert_(total_price_to_be_paid == 190000, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(200001)
        self.assert_(total_price_to_be_paid == 190001, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(200002)
        self.assert_(total_price_to_be_paid == 190002, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(100000)
        self.assert_(total_price_to_be_paid == 100000, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(300000)
        self.assert_(total_price_to_be_paid == 276000, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(500000)
        self.assert_(total_price_to_be_paid == 450000, f"{total_price_to_be_paid}")

        total_price_to_be_paid = discount_tier.getTotalPrice(600000)
        self.assert_(total_price_to_be_paid == 540000, f"{total_price_to_be_paid}")

if __name__ == '__main__':
    unittest.main()