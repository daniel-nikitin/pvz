from Plant import Plant
from Seed import Seed


class PeaShooter(Plant):
    def __init__(self):
        super().__init__(base_filename="graphics/Plants/Peashooter/Peashooter", number_of_textures=13)


class PeaShooterSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_peashooter.png", cost=100, cooldown=10.0)

    def create_plant(self):
        return PeaShooter()
