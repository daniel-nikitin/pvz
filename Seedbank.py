import arcade

from Seed import Seed
from hand import Hand

TIMER_SUN = 1.5


class Seedbank(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="graphics/Screen/SeedBank.png")
        self.number_of_suns = 100
        self.seeds = arcade.SpriteList()
        self.time_left_sun = TIMER_SUN

    def add(self, seed: Seed):
        self.seeds.append(seed)
        for n in range(len(self.seeds)):
            self.seeds[n].left = 75 + self.left + n * 55
            self.seeds[n].top = -5 + self.top

    def update_animation(self, delta_time: float = 1 / 60):
        self.seeds.update_animation(delta_time)
        self.update_suns(delta_time)

    def update_suns(self, delta_time):
        self.time_left_sun -= delta_time
        if self.time_left_sun <= 0:
            self.add_suns(1)
            self.time_left_sun = TIMER_SUN

    def on_draw(self):
        self.draw()
        self.seeds.draw()
        self.draw_overlay()
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
                if s.cost <= self.number_of_suns:
                    s.on_mouse_press(x, y, put_in_hand)

    def buy(self, hand: Hand) -> Seed:
        seed = hand.release()
        if seed is not None:
            if seed.cost > self.number_of_suns:
                return
            self.number_of_suns -= seed.cost
            seed.start_cooldown()
        return seed

    def add_suns(self, how_much: int):
        self.number_of_suns += how_much

    def draw_overlay(self):
        for i in self.seeds:
            i: Seed
            if i.cost > self.number_of_suns:
                arcade.draw_lrtb_rectangle_filled(
                    left=i.left,
                    right=i.right,
                    bottom=i.bottom,
                    top=i.bottom + i.height,
                    color=[0, 0, 0, 128]
                )
            arcade.draw_lrtb_rectangle_filled(
                left=i.left,
                right=i.right,
                bottom=i.bottom,
                top=i.bottom + i.height * i.cool_down(),
                color=[0, 0, 0, 128]
            )
