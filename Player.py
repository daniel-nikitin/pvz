from AnimatedSprite import AnimatedSprite


class Player(AnimatedSprite):
    def __init__(self, base_filename: str, number_of_textures: int, health: int):
        super().__init__(base_filename=base_filename, number_of_textures=number_of_textures)
        self.health = health
        self.hurting = False
        self.reset_hurt_timer()
        self.hurt_timer = 0.0
        self.initial_color = self.color

    def hurt(self, damage: int):
        if self.hurting:
            return
        if damage > 0:
            self.hurting = True
            self.health -= damage

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        if self.hurting:
            self.color = (255, 0, 0)
            self.hurt_timer -= delta_time
        else:
            self.color = self.initial_color
        if self.hurt_timer < 0:
            self.hurting = False
            self.reset_hurt_timer()

        if self.health <= 0:
            self.kill()

    def reset_hurt_timer(self):
        self.hurt_timer = 0.2
