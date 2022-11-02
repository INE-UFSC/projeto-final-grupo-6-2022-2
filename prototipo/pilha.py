import pygame
from item import Item

class Pilha(Item):
    def __init__(self, x, y, sprite, grupo, nivel, status = True):
        super().__init__(x, y, sprite, grupo)
        self.nivel = nivel
        self.tempo_restante = nivel*30
        self.tamanho = [nivel*5,20]
        self.__status = status
        self.__usando = False

    def getStatus(self):
        return self.__status
    
    def setUsando(self, usando):
        self.__usando = usando
    
    def usar(self):
        print("usado pilha")
        self.kill()
    
    def contador(self):
        if self.__usando:
            self.tempo_restante -= 1
        
        if self.tempo_restante == 0:
            self.__status = False
    
        tela = pygame.display.get_surface()
        self.draw_timer(tela)

    def draw_timer(self, tela):
        if self.__status:
            pygame.draw.rect(tela, (0, 0, 255), (10, 10, self.tamanho[0], self.tamanho[1]))
            pygame.draw.rect(tela, (0, 255, 0), (10, 10, self.tempo_restante/6, self.tamanho[1]))
        else:
            pygame.draw.rect(tela, (255, 0, 0), (10, 10, self.tamanho[0], self.tamanho[1]))
