import pygame   
import jogador
from pilha import Pilha
from settings import WIDTH, HEIGTH

class Lanterna(pygame.sprite.Sprite):
    def __init__(self, pos, status = False, tempo_ligada = 0):
        super().__init__(pygame.sprite.Group())
        
        self.cor = (0, 255, 255)
        self.__status = status
        self.pilha = Pilha(pos[0],pos[1],'tiles/pilha.png', pygame.sprite.Group(), 50)
        self.tempo_ligada = tempo_ligada
        
        self.image = pygame.image.load('tiles/light.png').convert_alpha()
        self.rect = self.image.get_rect()
        
        self.__x = (WIDTH-self.rect[2])/2
        self.__y = (HEIGTH-self.rect[3])/2
        #self.hitbox = self.rect.inflate(0,-26)
    
    def update(self):
        self.pilha.contador()
    
    def setPos(self, x, y):
        self.hitbox.x = x
        self.hitbox.y = y
    
    def getStatus(self):
        return self.__status

    def setStatus(self):
        self.__status = not self.__status
        self.pilha.setUsando(self.__status)

    def draw(self, tela):
        if self.__status:
            tela.blit(self.image, (self.__x, self.__y))
        else:
            pygame.draw.rect(tela, (0,0,0),(0,0, WIDTH, HEIGTH))