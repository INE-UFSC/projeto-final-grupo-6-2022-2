from weapon import Weapon


class ProjectileWeapon(Weapon):

    def __init__(self, x, y, name, damage, shot_speed):
        super().__init__(x, y, f'tiles/{name}.png')
        self.__name = name
        self.__damage = damage
        self.__shot_speed = shot_speed

    def attack(self):
        return (f'tile/{self.__name}_projectile.png', self.__damage, self.__shot_speed)
