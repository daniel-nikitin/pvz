from AnimatedSprite import AnimatedSprite


class Sun(AnimatedSprite):
    def __init__(self, x: int, y: int, target_x: float, target_y: float):
        super().__init__(base_filename="graphics/Plants/Sun/Sun", number_of_textures=22)
        self.center_x = x
        self.center_y = y
        self.start_x = x
        self.start_y = y
        self.target_x = target_x
        self.target_y = target_y
        self.change_x = (target_x - x) / 100
        self.change_y = (target_y - y) / 100

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        if self.center_y > self.target_y:
            self.center_x = self.start_x
            self.center_y = self.start_y
