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

    def getDiscount(self, amount: int) -> int:
        self.discount_tiers.sort(key=lambda x: x.amount, reverse=True)
        discount = -1
        i = 0
        while discount == -1:
            
            if amount >= self.discount_tiers[i].amount:
                discount = int(amount * self.discount_tiers[i].discount)
            elif i == len(self.discount_tiers) - 1:
                discount = 0
            i+=1
                
        return discount

    def getTotalPrice(self, amount: int) -> int:
        return amount - self.getDiscount(amount)
    
    
    

