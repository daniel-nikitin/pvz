import arcade

from Seed import Seed
from hand import Hand


class Seedbank(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="graphics/Screen/SeedBank.png")
        self.number_of_suns = 100
        self.seeds = arcade.SpriteList()

    def add(self, seed: Seed):
        self.seeds.append(seed)
        for n in range(len(self.seeds)):
            self.seeds[n].left = 75 + self.left + n * 55
            self.seeds[n].top = -5 + self.top

    def update_animation(self, delta_time: float = 1 / 60):
        self.seeds.update_animation(delta_time)

    def on_draw(self):
        self.draw()
        self.seeds.draw()
        arcade.draw_text(
            text=self.number_of_suns,
            start_x=self.left + 20,
            start_y=self.bottom + 10,
            color=arcade.csscolor.RED
        )

    def on_mouse_press(self, x, y, put_in_hand):
        if self.collides_with_point((x, y)):
            for s in self.seeds:
                s: Seed
                s.on_mouse_press(x, y, put_in_hand)

    def buy(self, hand: Hand) -> Seed:
        seed = hand.release()
        if seed is not None:
            self.number_of_suns -= seed.cost
            seed.start_cooldown()
        return seed
