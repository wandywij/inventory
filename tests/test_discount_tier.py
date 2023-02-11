
from cashier.module.discount_tier import DiscountTier
import unittest

class TestDiscountTier(unittest.TestCase):
    

    def test_discount_tier(self):
        discount_tier = DiscountTier()
        
        total_price_to_be_paid = discount_tier.getTotalPrice(200000)
        assert(total_price_to_be_paid == 190000)

        total_price_to_be_paid = discount_tier.getTotalPrice(200001)
        assert(total_price_to_be_paid == 190001)

        total_price_to_be_paid = discount_tier.getTotalPrice(200002)
        assert(total_price_to_be_paid == 190002)

        total_price_to_be_paid = discount_tier.getTotalPrice(100000)
        assert(total_price_to_be_paid == 100000)

        total_price_to_be_paid = discount_tier.getTotalPrice(300000)
        assert(total_price_to_be_paid == 276000)

        total_price_to_be_paid = discount_tier.getTotalPrice(500000)
        assert(total_price_to_be_paid == 450000)

        total_price_to_be_paid = discount_tier.getTotalPrice(600000)
        assert(total_price_to_be_paid == 540000)

if __name__ == '__main__':
    unittest.main()