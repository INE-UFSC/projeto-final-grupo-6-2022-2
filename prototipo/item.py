import pygame
from pilha import Pilha

class Item(pygame.sprite.Sprite):
    def  __init__(self, x, y, tamanho, cor, tipo, sprite, grupo):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(grupo)
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = cor
        self.tipo = tipo
        self.sprite = sprite
        self.image = self.image = pygame.image.load(sprite).convert_alpha()
        self.image.fill(self.cor)
        self.image = pygame.Surface(self.tamanho)
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.posicao = [self.x, self.y]
    
    
    def pegar_item(self, jogador):
        if jogador.x == self.x and jogador.y == self.y:
            if self.tipo == "pilha":
                jogador.pilha = Pilha(100, False, False, 10, [100, 20], 0, 0)
                self.kill()
