from Plant import Plant
from Seed import Seed


class Sunflower(Plant):
    def __init__(self):
        super().__init__(base_filename="graphics/Plants/SunFlower/SunFlower", number_of_textures=18)


class SunflowerSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_sunflower.png", cost=50, cooldown=5.0)

    def create_plant(self):
        return Sunflower()
