from AnimatedSprite import AnimatedSprite


class Zombie(AnimatedSprite):
    def __init__(self):
        super().__init__(base_filename="graphics/Zombies/NormalZombie/Zombie/Zombie", number_of_textures=22)
        self.change_x = -1
