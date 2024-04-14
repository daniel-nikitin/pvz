from Plant import Plant
from Seed import Seed

TIMER_SUN = .5


class Sunflower(Plant):
    def __init__(self):
        super().__init__(base_filename="graphics/Plants/SunFlower/SunFlower", number_of_textures=18)
        self.time_left_sun = TIMER_SUN
        self.suns = 0

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        self.time_left_sun -= delta_time
        if self.time_left_sun <= 0:
            self.suns += 1
            self.time_left_sun = TIMER_SUN

    def give_all_suns(self):
        how_many_to_givaway = self.suns
        self.suns = 0
        return how_many_to_givaway


class SunflowerSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_sunflower.png", cost=50, cooldown=5.0)

    def create_plant(self):
        return Sunflower()
