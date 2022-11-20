import pygame

from abstractInterface import AbstractInterface
from button import Button

class ControlsInterface(AbstractInterface):
    def __init__(self, screen, file_background_image):
        super().__init__(screen, file_background_image)
        self.buttons = pygame.sprite.Group([Button(100, 80, 'prototipo\\tiles\\rock.png', 'prototipo\\tiles\porta.png')])
    
    def start(self, clock):
        run = True
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if event.button == 1 and button.colliding():
                            print('voltar para janela anterior')
            
            self.draw()
            pygame.display.flip()
    
    def draw(self):
        self.buttons.update()
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, ((1280-self.background.get_rect()[2])//2,0))
        self.buttons.draw(self.screen)