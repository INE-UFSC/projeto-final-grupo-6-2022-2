import pygame
from item import Item

class Pilha(Item):
    def __init__(self, x, y, sprite, nivel, status = True):
        super().__init__(x, y, sprite)
        self.nivel = nivel
        self.tempo_restante = nivel*30
        self.tamanho = [nivel*5,10]
        self.__status = status
        self.__usando = False
        self.image = pygame.image.load('tiles/pilha.png').convert_alpha()
        self.hud_vida = pygame.image.load('tiles/hud_vida.png').convert_alpha() 

    def getStatus(self):
        return self.__status
    
    def setUsando(self, usando):
        self.__usando = usando
    
    def getUsando(self):
        return self.__usando
    
    def use(self, jogador):
        jogador.getLight().setPilha(self)
        self.kill()
    
    def contador(self):
        if self.__usando:
            self.tempo_restante -= 1
        
        if self.tempo_restante == 0:
            self.__status = False
    
        tela = pygame.display.get_surface()
        self.draw_timer(tela)

        
    def draw_timer(self, surface):
        

        if self.__status:
            pygame.draw.rect(surface, (0, 0, 255), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))
            pygame.draw.rect(surface, (0, 255, 0), (2, 15, self.tempo_restante/6 - 10, self.tamanho[1]))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (2, 15, self.tamanho[0] - 10, self.tamanho[1]))

        x =0
        y = 0
        display = pygame.display.get_surface()
        display.blit(self.hud_vida, (x, y))
        

        
