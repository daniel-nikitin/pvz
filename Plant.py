import arcade


class Plant(arcade.Sprite):
    def __init__(self, filename, number_of_textures=18):
        super().__init__(filename=filename)
        self.number_of_textures = number_of_textures
