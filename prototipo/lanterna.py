import pygame   
import jogador
from pilha import Pilha


class Lanterna(pygame.sprite.Sprite):
    def __init__(self, pos, status = False, pilha = None, tempo_ligada = 0):
        super().__init__(pygame.sprite.Group())
        self.__x = pos[0]
        self.__y = pos[1]
        self.cor = (0, 255, 255)
        self.__status = status
        self.pilha = pilha
        self.tempo_ligada = tempo_ligada
        
        self.image = pygame.image.load('tiles/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.__x, self.__y))
        #self.hitbox = self.rect.inflate(0,-26)
     
    def setPos(self, x, y):
        self.__x = 640-32
        self.__y = 360-19
    
    def getStatus(self):
        return self.__status

    def setStatus(self):
        self.__status = not self.__status

    def draw(self, tela):
        if self.__status:
            tela.blit(self.image, (640-32, 360-19))
