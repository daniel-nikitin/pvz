from Plant import Plant
from Seed import Seed


class Hand:
    def __init__(self):
        self.seed = None
        self.seed: Seed
        self.plant = None
        self.plant: Plant
        self.center_x = 0
        self.center_y = 0

    def draw(self):
        if self.plant is not None:
            self.plant.center_x = self.center_x
            self.plant.center_y = self.center_y
            self.plant.draw()

    def take(self, seed: Seed):
        self.seed = seed
        self.plant = seed.create_plant()

    def release(self) -> Seed:
        s = self.seed
        self.seed = None
        self.plant = None
        return s
