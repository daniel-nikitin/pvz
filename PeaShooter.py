from AnimatedSprite import AnimatedSprite
from Plant import Plant
from Seed import Seed

TIMER_BULLET = 2


class PeaShooter(Plant):
    def __init__(self):
        super().__init__(base_filename="graphics/Plants/Peashooter/Peashooter", number_of_textures=13)
        self.cooldown_time = TIMER_BULLET
        self.bullets = 0

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        self.cooldown_time -= delta_time
        if self.cooldown_time <= 0:
            self.bullets += 1
            self.cooldown_time = TIMER_BULLET

    def shoot_all_bullets(self):
        how_many_to_givaway = self.bullets
        self.bullets = 0
        return how_many_to_givaway


class PeaShooterSeed(Seed):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_peashooter.png", cost=100, cooldown=10.0)

    def create_plant(self):
        return PeaShooter()


class PeashooterBullet(AnimatedSprite):
    def __init__(self, x, y):
        super().__init__(base_filename="graphics/Bullets/PeaNormal/PeaNormal", number_of_textures=1)
        self.change_x = 10

        self.set_position(x, y)
