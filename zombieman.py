from AnimatedSprite import AnimatedSprite


class Zombie(AnimatedSprite):
    def __init__(self,
                 base_filename,
                 number_of_textures,
                 health
                 ):
        super().__init__(base_filename=base_filename, number_of_textures=number_of_textures)
        self.change_x = -1
        self.health = health
        self.hurting = False
        self.reset_timer()
        self.initial_color = self.color

    def hurt(self, damage: int):
        if self.hurting:
            return
        self.hurting = True
        self.health -= damage

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        if self.hurting:
            self.color = (255, 0, 0)
            self.timer -= delta_time
        else:
            self.color = self.initial_color
        if self.timer < 0:
            self.hurting = False
            self.reset_timer()

        if self.health <= 0:
            self.kill()

    def reset_timer(self):
        self.timer = 0.2


class BucketheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie",
            number_of_textures=15,
            health=200
        )


class ConeheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie",
            number_of_textures=21,
            health=105
        )


class NormalZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/NormalZombie/Zombie/Zombie",
            number_of_textures=22,
            health=100
        )
