from math import ceil
try:
    from discount import Discount
except:
    from cashier.module.discount import Discount

class DiscountTier:
    discount_tiers = [Discount(200000, 0.05),
                      Discount(300000, 0.08), 
                      Discount(500000, 0.1)]

    def __init__(self) -> None:
        pass

    def getTotalPrice(self, amount: int) -> int:
        self.discount_tiers.sort(key=lambda x: x.amount, reverse=True)
        amount_to_be_paid = 0
        i = 0
        while amount_to_be_paid == 0:
            if amount >= self.discount_tiers[i].amount:
                amount_to_be_paid = ceil(amount - (amount * self.discount_tiers[i].discount)) 
            elif i == len(self.discount_tiers) - 1:
                amount_to_be_paid = amount
            else:
                i+=1
        return amount_to_be_paid
