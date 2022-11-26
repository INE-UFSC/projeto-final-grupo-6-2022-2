from weapon import Weapon


class ProjectileWeapon(Weapon):

    def __init__(self, x, y, name):
        super().__init__(x, y, f'tiles/{name}.png')
        self.__name = name

    # retorna o path do sprite para que level instancie o projetil
    # ideia em desenvolvimento
    def attack(self):
        return f'tile/{self.__name}_projectile.png'
