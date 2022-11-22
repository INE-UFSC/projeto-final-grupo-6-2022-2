import pygame

from abstractInterface import AbstractInterface
from button import Button

class ControlsInterface(AbstractInterface):
    def __init__(self, screen, file_background_image):
        super().__init__(screen, file_background_image)
        self.__buttons = pygame.sprite.Group([Button(420, 90, 'prototipo\interfaces\setaControleMouseSelecionado.png', 'prototipo\interfaces\setaControleSemMouse.png')])
    
    def start(self, clock):
        run = True
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.__buttons:
                        if event.button == 1 and button.colliding():
                            print('voltar para janela anterior')
                            return

            self.draw()
            pygame.display.flip()
    
    def draw(self):
        self.__buttons.update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.__buttons.draw(self.getScreen())
       
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
tela = ControlsInterface(window, 'prototipo\interfaces\Captura de tela_20221104_205804.png')
tela.start(clock)