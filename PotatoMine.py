from Plant import Plant
from Seed import Seed


class Potatomine(Plant):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Plants/PotatoMine/PotatoMine/PotatoMine",
            number_of_textures=8,
            health=1
        )


class PotatoMineSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_potatomine.png", cost=25, cooldown=15.0)

    def create_plant(self):
        return Potatomine()
