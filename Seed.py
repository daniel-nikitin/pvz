from abc import abstractmethod, ABC

import arcade

from Plant import Plant


class Seed(arcade.Sprite, ABC):
    def __init__(self, filename, cost):
        super().__init__(filename=filename, scale=0.84)
        self.cost = cost

    def on_mouse_press(self, x, y, put_in_hand):
        if self.collides_with_point((x, y)):
            p = self.create_plant()
            p.center_x = x
            p.center_y = y
            put_in_hand(self)

    @abstractmethod
    def create_plant(self) -> Plant:
        pass
