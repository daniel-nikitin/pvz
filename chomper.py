from Plant import Plant
from Seed import Seed


class Chomper(Plant):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Plants/Chomper/Chomper/Chomper",
            number_of_textures=13,
            health=100
        )


class ChomperSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_chomper.png", cost=150, cooldown=15.0)

    def create_plant(self):
        return Chomper()
