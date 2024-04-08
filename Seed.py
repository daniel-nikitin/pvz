from abc import abstractmethod, ABC

import arcade

from Plant import Plant


class Seed(arcade.Sprite, ABC):
    def __init__(self, filename, cost, cooldown):
        super().__init__(filename=filename, scale=0.84)
        self.cooldown = cooldown
        self.cost = cost
        self.cooldown_left = 0.0

    def on_mouse_press(self, x, y, put_in_hand):
        if self.collides_with_point((x, y)) and self.cooldown_left <= 0.0:
            p = self.create_plant()
            p.center_x = x
            p.center_y = y
            put_in_hand(self)

    def update_animation(self, delta_time: float = 1 / 60):
        self.cooldown_left -= delta_time

    def cool_down(self) -> float:
        if self.cooldown_left <= 0:
            return 0.0
        else:
            return self.cooldown_left / self.cooldown

    @abstractmethod
    def create_plant(self) -> Plant:
        pass

    def start_cooldown(self):
        self.cooldown_left = self.cooldown
