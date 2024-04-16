import arcade

ANIMATION_CYCLE_DURATION = .7


class AnimatedSprite(arcade.Sprite):
    def __init__(self, base_filename: str, number_of_textures: int):
        super().__init__(filename=base_filename + "_0.png")
        self.number_of_textures = number_of_textures
        self.time = 0.0
        for i in range(1, number_of_textures):
            self.textures.append(arcade.load_texture(base_filename + f"_{i}.png"))

    def update_animation(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.time += delta_time
        if self.time > ANIMATION_CYCLE_DURATION / self.number_of_textures:
            self.time = 0.0
            self.cur_texture_index += 1
            if self.cur_texture_index > self.number_of_textures - 1:
                self.cur_texture_index = 0
            self.texture = self.textures[self.cur_texture_index]
