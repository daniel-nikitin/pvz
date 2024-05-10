from typing import List

import arcade
from arcade import Texture

from Player import Player

TIMER_ATTACK = 2


class Zombie(Player):
    def __init__(
            self,
            base_filename: str,
            number_of_textures: int,
            health: int,
            speed: float,
            damage: int,
            base_filename_attack: str,
            number_of_textures_attack: int
    ):
        super().__init__(base_filename=base_filename, number_of_textures=number_of_textures, health=health)
        self.number_of_textures_attack = number_of_textures_attack
        self.base_filename_attack = base_filename_attack
        self.speed = speed
        self.damage = damage
        self.cooldown_time = TIMER_ATTACK
        self.attacking = False
        self.attack_textures: List[Texture] = []
        self.walking_textures = self.textures
        self.number_of_textures_walking = number_of_textures
        for i in range(1, number_of_textures_attack):
            self.attack_textures.append(arcade.load_texture(base_filename_attack + f"_{i}.png"))

    def attack(self):
        self.attacking = True
        if self.cooldown_time <= 0:
            self.cooldown_time = TIMER_ATTACK
            return self.damage
        else:
            return 0

    def walk(self):
        self.attacking = False

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        if self.attacking:
            self.textures = self.attack_textures
            self.number_of_textures = self.number_of_textures_attack
            self.stop()
        else:
            self.change_x = -self.speed
            self.textures = self.walking_textures
            self.number_of_textures = self.number_of_textures_walking
        self.cooldown_time -= delta_time


class BucketheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie",
            base_filename_attack="graphics/Zombies/BucketheadZombie/BucketheadZombieAttack/BucketheadZombieAttack",
            number_of_textures=15,
            number_of_textures_attack=11,
            health=200,
            speed=0.1,
            damage=100
        )


class ConeheadZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie",
            base_filename_attack="graphics/Zombies/ConeheadZombie/ConeheadZombieAttack/ConeheadZombieAttack",
            number_of_textures=21,
            number_of_textures_attack=11,
            health=105,
            speed=0.2,
            damage=5
        )


class NormalZombie(Zombie):
    def __init__(self):
        super().__init__(
            base_filename="graphics/Zombies/NormalZombie/Zombie/Zombie",
            base_filename_attack="graphics/Zombies/NormalZombie/ZombieAttack/ZombieAttack",
            number_of_textures=22,
            number_of_textures_attack=21,
            health=100,
            speed=0.5,
            damage=5
        )
