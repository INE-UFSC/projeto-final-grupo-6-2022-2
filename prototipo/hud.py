import pygame
from pilha import Pilha


class Hud():
    def __init__(self):
        self.__hud_pilha = pygame.image.load('tiles/hud_pilha.png').convert_alpha()
        self.__hud_vida = pygame.image.load('tiles/hud_vida.png').convert_alpha()
        self.__display = pygame.display.get_surface()



    def draw(self, player):
        self.draw_timer_pilha(player.getLight().pilha)
        self.draw_health(player.getHealth())



    def draw_timer_pilha(self, pilha):
        if pilha.getStatus():
            pygame.draw.rect(self.__display, (0, 0, 255), (2, 15, pilha.tamanho[0] - 10, pilha.tamanho[1]))
            pygame.draw.rect(self.__display, (0, 255, 0), (2, 15, pilha.tempo_restante/6 - 10, pilha.tamanho[1]))
        else:
            pygame.draw.rect(self.__display, (255, 0, 0), (2, 15, pilha.tamanho[0] - 10, pilha.tamanho[1]))
        
        x_pilha = 0
        y_pilha = 0
        self.__display.blit(self.__hud_pilha, (x_pilha, y_pilha))
            
    def draw_health(self, vida):
        x = 690
        y = 0

        x_barra = x+15
        y_barra = y+15
        width_barra = self.__hud_vida.get_width() - 20

        gordura_da_barra = 15
        vida_maxima = 100
        pygame.draw.rect(self.__display, (255, 0, 0), (x_barra, y_barra, width_barra, gordura_da_barra))
        pygame.draw.rect(self.__display, (0, 255, 0), (x_barra, y_barra, (width_barra / vida_maxima) * vida, gordura_da_barra))
        self.__display.blit(self.__hud_vida, (x, y))

    def update(self, pilha, vida):
        # self.__pilha.contador()
        self.draw(pilha, vida)
        self.draw_health(vida)



'''    def draw_timer(self, surface):
        
        if self.__status:
            pygame.draw.rect(surface, (0, 0, 255), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))
            pygame.draw.rect(surface, (0, 255, 0), (2, 15, self.tempo_restante/6 - 10, self.tamanho[1]))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))

        x =0
        y = 0
        display = pygame.display.get_surface()
        display.blit(self.hud_pilha, (x, y))
        '''