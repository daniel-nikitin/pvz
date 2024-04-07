from PotatoMine import Potatomine
from Seed import Seed


class PotatoMineSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_potatomine.png", cost=25)
        self.cooldown = 10.0

    def create_plant(self):
        return Potatomine()