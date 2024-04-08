from PeaShooter import PeaShooter
from Seed import Seed


class PeaShooterSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_peashooter.png", cost=100, cooldown=10.0)

    def create_plant(self):
        return PeaShooter()
