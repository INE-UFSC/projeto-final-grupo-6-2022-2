import pygame
from item import Item

class Pilha(Item):
    def __init__(self, x, y, sprite, grupo, nivel, status = True, tempo_restante = 10, tamanho = [100, 20]):
        super().__init__(x, y, sprite, grupo)
        self.nivel = nivel
        self.tempo_restante = tempo_restante
        self.tamanho = tamanho
        self.__status = status

    def getStatus(self):
        return self.__status
    
    def usar(self):
        print("usado pilha")
        self.kill()
    
    def update(self):
        pass

    def draw_timer(self, tela):
        pygame.draw.rect(tela, (0, 0, 255), (self.x + 10, self.y, self.tamanho[0], self.tamanho[1]))
        pygame.draw.rect(tela, (0, 255, 0), (self.x + 10, self.y, self.tamanho[0] * (self.tempo_restante / 10), self.tamanho[1]))
        pygame.draw.rect(tela, (255, 0, 0), (self.x + 10, self.y, self.tamanho[0] * (self.tempo_restante / 10), self.tamanho[1]), 1)
