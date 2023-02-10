
from src import discount_tier
from src import discount

discount_tier = discount_tier.DiscountTier()

def test_discount_tier():
    
    
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