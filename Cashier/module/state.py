from enum import Enum


class InputState(Enum):
    NAME = 1
    QUANTITY = 2
    PRICE = 3
    DONE=4

    currentState = NAME

    def update_state(self, oldState):
        if oldState == self.NAME:
           return self.QUANTITY
        elif oldState == self.QUANTITY:
            return self.PRICE
        elif oldState == self.PRICE:
            return self.DONE
