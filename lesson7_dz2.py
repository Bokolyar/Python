from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def calc(self):
        return self.V/6.5 + 0.5

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def calc(self):
        return self.H*2 + 0.3


Coat1 = Coat(13)
print(Coat1.calc)
Suit1 = Suit(2)
print(Suit1.calc)

print(f'Общий расход: {Coat1.calc+Suit1.calc}')