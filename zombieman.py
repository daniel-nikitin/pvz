from Player import Player

TIMER_ATTACK = 2


class Zombie(Player):
    def __init__(self, base_filename: str, number_of_textures: int, health: int, speed: float, damage: int):
        super().__init__(base_filename=base_filename, number_of_textures=number_of_textures, health=health)
        self.change_x = -speed
        self.damage = damage
        self.cooldown_time = TIMER_ATTACK

    def attack(self):
        if self.cooldown_time <= 0:
            self.cooldown_time = TIMER_ATTACK
            return self.damage
        else:
            return 0

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        self.cooldown_time -= delta_time


class BucketheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie",
            number_of_textures=15,
            health=200,
            speed=0.1,
            damage=100
        )


class ConeheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie",
            number_of_textures=21,
            health=105,
            speed=0.2,
            damage=5
        )


class NormalZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/NormalZombie/Zombie/Zombie",
            number_of_textures=22,
            health=100,
            speed=0.5,
            damage=5
        )
