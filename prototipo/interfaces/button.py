import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, fileHover, fileNormal):
        super().__init__()
        #Carregamento das imagens
        imgNormal = pygame.image.load(fileNormal).convert_alpha()
        imgHover = pygame.image.load(fileHover).convert_alpha()
        #Pegando os retângulos das imagens para determinar o tamanho das Surfaces
        rectNormal = imgNormal.get_rect()
        rectHover = imgHover.get_rect()
        #Imagem sem mouse por cima
        self.__original_image = pygame.Surface((rectNormal[2],rectNormal[3]))
        self.__original_image.set_colorkey((0,0,0))
        self.__original_image.blit(imgNormal, imgNormal.get_rect())
        #Imagem com mouse por cima
        self.__hover_image = pygame.Surface((rectHover[2], rectNormal[3]))
        self.__hover_image.set_colorkey((0,0,0))
        self.__hover_image.blit(imgHover, imgHover.get_rect())
        #Atributos usados para o draw
        self.__image = self.__original_image
        self.__rect = self.__image.get_rect(center = (x, y))

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    #Retorna True se o mouse estiver por cima
    def colliding(self) -> bool:
        return self.__rect.collidepoint(pygame.mouse.get_pos())
    
    #Atualiza a imagem que será carregada na tela
    def update(self):
        self.__image = self.__hover_image if self.colliding() else self.__original_image