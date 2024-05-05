import random

import arcade

from Bombcherry import BombcherrySeed
from PeaShooter import PeaShooterSeed, PeaShooter, PeashooterBullet
from PotatoMine import PotatoMineSeed
from Seed import Seed
from Seedbank import Seedbank
from Sun import Sun
from Sunflower import SunflowerSeed, Sunflower
from chomper import ChomperSeed
from hand import Hand
from zombieman import Zombie, BucketheadZombie, ConeheadZombie, NormalZombie


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.background = arcade.load_texture(
            file_name="graphics/Items/Background/Background_0.jpg",
            width=self.width,
            height=self.height,
            x=150
        )

        self.seed_bank = Seedbank()
        self.seed_bank.top = self.height
        self.seed_bank.left = 100
        self.seed_bank.add(ChomperSeed())
        self.seed_bank.add(PeaShooterSeed())
        self.seed_bank.add(SunflowerSeed())
        self.seed_bank.add(BombcherrySeed())
        self.seed_bank.add(PotatoMineSeed())

        self.hand = Hand()

        self.plants = arcade.SpriteList()
        self.suns = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.add_zombies(10)

    def add_zombies(self, number_of_zombie):
        typesofzombies = [BucketheadZombie, ConeheadZombie, NormalZombie]
        for i in range(number_of_zombie):
            zombietype = random.choice(typesofzombies)
            zombie = zombietype()
            zombie.center_x = 1000
            zombie.center_y = random.randint(41, 521)
            self.zombies.append(zombie)

    def when_sun_reach_seedbank(self, sun: Sun):
        self.seed_bank.add_suns(sun.how_many)
        sun.kill()

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background)
        self.seed_bank.on_draw()
        self.hand.draw()
        self.bullets.draw()
        self.plants.draw()
        self.zombies.draw()
        self.suns.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.check_bullets_collision()
        self.plants.update_animation(delta_time)
        self.seed_bank.update_animation(delta_time)
        self.suns.update_animation(delta_time)
        self.zombies.update_animation(delta_time)
        self.bullets.update_animation(delta_time)

        for i in self.plants:
            if isinstance(i, Sunflower):
                i: Sunflower
                harvested = i.give_all_suns()
                if harvested > 0:
                    self.suns.append(Sun(
                        x=i.center_x,
                        y=i.center_y,
                        target_x=self.seed_bank.left + 45,
                        target_y=self.seed_bank.bottom + 50,
                        when_target_reached=self.when_sun_reach_seedbank,
                        how_many=harvested
                    ))

            if isinstance(i, PeaShooter):
                i: PeaShooter
                shot = i.shoot_all_bullets()
                if shot > 0:
                    self.bullets.append(PeashooterBullet(
                        x=i.center_x + 20,
                        y=i.center_y + 20,
                    ))

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.hand.center_x = x
        self.hand.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.seed_bank.on_mouse_press(x, y, self.put_in_hand)
        print(y)

    def on_mouse_release(self, x, y, button, key_modifiers):
        seed = self.seed_bank.buy(self.hand)
        if seed is not None:
            plant = seed.create_plant()
            plant.center_x = x
            plant.center_y = y
            self.plants.append(plant)

    def check_bullets_collision(self):
        for b in self.bullets:
            b: PeashooterBullet
            if not b.exploded:
                hits = arcade.check_for_collision_with_list(sprite=b, sprite_list=self.zombies)
                if len(hits) > 0:
                    zombie = hits[0]
                    zombie: Zombie
                    b.explode()
                    zombie.hurt(20)

    def put_in_hand(self, seed: Seed):
        self.hand.take(seed)
