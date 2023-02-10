from math import ceil
from src import discount

class DiscountTier:
    discount_tiers = [discount.Discount(200000, 0.05),
                      discount.Discount(300000, 0.08), 
                      discount.Discount(500000, 0.1)]

    def __init__(self) -> None:
        pass

    def getTotalPrice(self, amount: int) -> int:
        self.discount_tiers.sort(key=lambda x: x.amount, reverse=True)
        amount_to_be_paid = 0
        i = 0
        while amount_to_be_paid == 0:
            if amount >= self.discount_tiers[i].amount:
                amount_to_be_paid = ceil(amount - (amount * self.discount_tiers[i].discount)) 
            elif i == len(self.discount_tiers):
                amount_to_be_paid = amount
            else:
                i+=1
        return amount_to_be_paid
