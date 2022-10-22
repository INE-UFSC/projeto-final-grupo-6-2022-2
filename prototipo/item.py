import pygame
from pilha import Pilha

class Item(pygame.sprite.Sprite):
    def  __init__(self, x, y, sprite,grupo):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(grupo)
        self.x = x
        self.y = y
        self.sprite = sprite
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.hitbox = self.rect.inflate(0,0)
        self.posicao = [self.x, self.y]
    
    def usar(self, jogador):
        #Só teste. Essa funcão aqui deve ser um abstract method
        jogador.pilha = Pilha(100, False, False, 10, [100, 20], 0, 0)
        self.kill()
        
    def exclui(self):
        self.kill()
