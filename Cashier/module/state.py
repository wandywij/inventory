from enum import Enum

# This is a simple Finite State Machine https://en.wikipedia.org/wiki/Finite-state_machine
# This is to make sure one state can only change to a specific state
class InputState(Enum):
    NAME = 1
    QUANTITY = 2
    PRICE = 3
    DONE= 4

    currentState = NAME

    def update_state(self, oldState):
        if oldState == self.NAME:
           return self.QUANTITY
        elif oldState == self.QUANTITY:
            return self.PRICE
        elif oldState == self.PRICE:
            return self.DONE
