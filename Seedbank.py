import arcade

from Seed import Seed


class Seedbank(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="graphics/Screen/SeedBank.png")
        self.number_of_suns = 0
        self.seeds = arcade.SpriteList()

    def add(self, seed: Seed):
        self.seeds.append(seed)

    def update_animation(self, delta_time: float = 1 / 60):
        for n in range(len(self.seeds)):
            self.seeds[n].left = 75 + self.left + n * 55
            self.seeds[n].top = -5 + self.top

    def on_draw(self):
        self.draw()
        self.seeds.draw()

    def on_mouse_press(self, x, y):
        if self.collides_with_point((x, y)):
            for seed in self.seeds:
                seed.on_mouse_press(x, y)
