from Seed import Seed


class SunflowerSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_sunflower.png")
        self.cost = 50
        self.cooldown = 5.0
