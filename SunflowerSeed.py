from Seed import Seed
from Sunflower import Sunflower


class SunflowerSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_sunflower.png")
        self.cost = 50
        self.cooldown = 5.0

    def create_plant(self):
        return Sunflower()
