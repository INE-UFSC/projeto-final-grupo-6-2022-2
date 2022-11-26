import pygame
from item import Item
from pygame import mixer 
from sound import Sound
mixer.init()


class Pilha(Item):
    # SEGUINTE AMIGOS
    # ISSO AQUI É UM ITEM QUE FICA NO CHAO
    # OU SEJA
    # ELE NAO DEVE GERENCIAR A LANTERNA
    # ELE DEVE SER SO UM ITEM Q É PEGO DO CHAO
    # E SO
    # PORQUE QUE TEM O CONTADOR AQUI?
    # VCS DEVERIAM CRIAR UMA CLASSE QUE GERENCIA A CARGA DA LANTERNA
    def __init__(self, x, y, sprite, nivel, status = True):
        super().__init__(x, y, sprite)
        self.__som = Sound('pilha')
        self.__sem_pilha = Sound('sem_pilha')
        self.nivel = nivel
        self.tempo_restante = nivel*30
        self.tamanho = [nivel*5,10]
        self.__status = status
        self.__usando = False
        self.image = pygame.image.load('tiles/pilha.png').convert_alpha()
        self.hud_pilha = pygame.image.load('tiles/hud_pilha.png').convert_alpha() 

    def getStatus(self):
        return self.__status
    
    def getTamanho(self):
        return self.tamanho
    
    def getTempoRestante(self):
        return self.tempo_restante
    
    def setUsando(self, usando):
        self.__usando = usando
    
    def getUsando(self):
        return self.__usando
    
    def use(self, jogador):
        jogador.getLight().setPilha(self)
        # Toca o som
        self.__som.play()
        self.kill()
    
    def contador(self):
        if self.__usando:
            self.tempo_restante -= 1
        
        if self.tempo_restante == 0:
            self.__status = False
            self.__sem_pilha.play()

    

    
        


        
