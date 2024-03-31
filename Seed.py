import arcade


class Seed(arcade.Sprite):
    def __init__(self, filename):
        super().__init__(filename=filename, scale=0.84)

    def on_mouse_press(self, x, y):
        if self.collides_with_point((x, y)):
            print(self)
