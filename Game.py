import arcade

from Bombcherry import BombcherrySeed
from PeaShooter import PeaShooterSeed
from PotatoMine import PotatoMineSeed
from Seed import Seed
from Seedbank import Seedbank
from Sunflower import SunflowerSeed, Sunflower
from chomper import ChomperSeed
from hand import Hand


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

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background)
        self.seed_bank.on_draw()
        self.hand.draw()
        self.plants.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.plants.update_animation(delta_time)
        self.seed_bank.update_animation(delta_time)
        for i in self.plants:
            if isinstance(i, Sunflower):
                i: Sunflower
                harvested = i.give_all_suns()
                self.seed_bank.add_suns(harvested)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.hand.center_x = x
        self.hand.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.seed_bank.on_mouse_press(x, y, self.put_in_hand)

    def on_mouse_release(self, x, y, button, key_modifiers):
        seed = self.seed_bank.buy(self.hand)
        if seed is not None:
            plant = seed.create_plant()
            plant.center_x = x
            plant.center_y = y
            self.plants.append(plant)

    def put_in_hand(self, seed: Seed):
        self.hand.take(seed)
