import pygame
from pilha import Pilha


class Hud():
    def __init__(self):
        self.__hud_vida = pygame.image.load('tiles/hud_vida.png').convert_alpha()
        self.__display = pygame.display.get_surface()



    def draw(self, pilha):
        self.draw_timer_pilha(pilha)
        x = 0
        y = 0
        self.__display.blit(self.__hud_vida, (x, y))


    def draw_timer_pilha(self, pilha):
        if pilha.getStatus():
            pygame.draw.rect(self.__display, (0, 0, 255), (2, 15, pilha.tamanho[0] - 10, pilha.tamanho[1]))
            pygame.draw.rect(self.__display, (0, 255, 0), (2, 15, pilha.tempo_restante/6 - 10, pilha.tamanho[1]))
        else:
            pygame.draw.rect(self.__display, (255, 0, 0), (2, 15, pilha.tamanho[0] - 10, pilha.tamanho[1]))


    def draw_health(self):
        pass


    def update(self, pilha):
        # self.__pilha.contador()
        self.draw(pilha)



'''    def draw_timer(self, surface):
        
        if self.__status:
            pygame.draw.rect(surface, (0, 0, 255), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))
            pygame.draw.rect(surface, (0, 255, 0), (2, 15, self.tempo_restante/6 - 10, self.tamanho[1]))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))

        x =0
        y = 0
        display = pygame.display.get_surface()
        display.blit(self.hud_vida, (x, y))
        '''