import arcade


class PeaShooterSeed(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="graphics/Cards/card_peashooter.png", scale=0.84)
        self.cost = 100
        self.cooldown = 10.0
