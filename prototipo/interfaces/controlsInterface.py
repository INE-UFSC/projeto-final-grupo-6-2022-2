import pygame

class ControlsInterface:
    def __init__(self):
        imgControle = pygame.image.load('prototipo\interfaces\Captura de tela_20221104_205804.png')
        self.__rect = imgControle.get_rect()
        self.__active = False
        self.__image = pygame.Surface((self.__rect[2], 720))
        self.__image.blit(imgControle, (0, (720 - self.__rect[3])/2))
    
    def setActive(self):
        self.__active = not self.__active
    
    def draw(self, screen):
        if self.__active:

            screen.blit(self.__image, (1280 - self.__rect[2], 0))
      
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
controles = ControlsInterface()
run = True
while run:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            controles.setActive()
            
    window.fill((157,15,15))
    controles.draw(window)
    pygame.display.flip()
