from Plant import Plant
from Seed import Seed


class Bombcherry(Plant):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Plants/CherryBomb/CherryBomb",
            number_of_textures=6,
            health=10
        )


class BombcherrySeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_cherrybomb.png", cost=150, cooldown=20.0)

    def create_plant(self):
        return Bombcherry()
