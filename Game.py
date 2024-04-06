import arcade

from PeaShooterSeed import PeaShooterSeed
from Plant import Plant
from Seedbank import Seedbank
from SunflowerSeed import SunflowerSeed


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
        self.seed_bank.add(SunflowerSeed())
        self.seed_bank.add(PeaShooterSeed())
        self.seed_bank.add(PeaShooterSeed())
        self.seed_bank.add(SunflowerSeed())
        self.seed_bank.add(SunflowerSeed())
        self.seed_bank.add(PeaShooterSeed())

        self.hand_mouse = None

        self.plants = arcade.SpriteList()

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background)
        self.seed_bank.on_draw()
        if self.hand_mouse is not None:
            self.hand_mouse.draw()
        self.plants.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.plants.update_animation(delta_time)
        self.seed_bank.update_animation(delta_time)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        if self.hand_mouse is not None:
            self.hand_mouse.center_x = x
            self.hand_mouse.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.seed_bank.on_mouse_press(x, y, self.put_in_hand)

    def on_mouse_release(self, x, y, button, key_modifiers):
        if self.hand_mouse is not None:
            self.plants.append(self.hand_mouse)
            self.hand_mouse = None

    def put_in_hand(self, plant: Plant):
        self.hand_mouse = plant
