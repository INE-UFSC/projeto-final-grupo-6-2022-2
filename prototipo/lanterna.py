import pygame   
import jogador
from pilha import Pilha


class Lanterna:
    def __init__(self, x, y, cor, tamanho, group, status = False, pilha = None, tempo_ligada = 0):
        self.x = x
        self.y = y
        self.cor = cor
        self.tamanho = tamanho
        self.status = status
        self.pilha = pilha
        self.tempo_ligada = tempo_ligada
        self.image = pygame.image.load('tiles/lanterna.png')
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.hitbox = self.rect.inflate(0,-26)
     
    def draw(self, pos, tela):
        pygame.draw.rect(tela, self.cor, (pos[0], pos[1], self.tamanho[0], self.tamanho[1]))


