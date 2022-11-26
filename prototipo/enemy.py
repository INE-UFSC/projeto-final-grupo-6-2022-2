from character import Character
from abc import abstractmethod


class Enemy(Character):

    def __init__(self, health: int, pos: tuple, speed: int, sprite: str, damage: int, obstacle_sprites, player):
        super().__init__(health, pos, speed, sprite, obstacle_sprites)
        self.__player = player
        self.__awake = False
        self.__damage = damage

    def attack(self, player):
        player.receiveDamage(self.__damage)

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in (list(self.getObstacleSprites()) + [self.__player]):
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.getDirectionX() > 0: # Se mover para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.getDirectionX() < 0: # Se mover para a esquerda
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in (list(self.getObstacleSprites()) + [self.__player]):
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.getDirectionY() > 0: # Se mover para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.getDirectionY() < 0: # Se mover para cima
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.cooldowns()
        self.reactToLight()
        self.move(self.getSpeed())

    @abstractmethod
    def reactToLight(self):
        pass
    
    def getPlayer(self):
        return self.__player
    
