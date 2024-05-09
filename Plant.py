from Player import Player

ANIMATION_CYCLE_DURATION = .7


class Plant(Player):
    def __init__(self, base_filename: str, number_of_textures: int, health: int):
        super().__init__(base_filename=base_filename, number_of_textures=number_of_textures, health=health)
