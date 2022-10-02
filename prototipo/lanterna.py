import pygame   
import jogador
from pilha import Pilha


class Lanterna:
    def __init__(self, x, y, cor, tamanho, status = False, pilha = Pilha(100), tempo_ligada = 0):
        self.x = x
        self.y = y
        self.cor = cor
        self.tamanho = tamanho
        self.status = status
        self.pilha = pilha
        self.tempo_ligada = tempo_ligada
        
     
    def lanterna(self, tela):
        if self.status:
            pygame.draw.rect(tela, self.cor, (jogador.x, jogador.y, self.tamanho[0], self.tamanho[1]))


