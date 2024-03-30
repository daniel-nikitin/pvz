import arcade

from Seed import PeaShooterSeed
from Seedbank import Seedbank

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PVZ"


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
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.seed_bank.add(PeaShooterSeed())
        self.seed_bank.add(PeaShooterSeed())
        self.seed_bank.add(PeaShooterSeed())

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background)
        self.seed_bank.on_draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.seed_bank.update_animation(delta_time)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
