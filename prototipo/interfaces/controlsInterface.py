import pygame

from interfaces.internalInterface import InternalInterface
from interfaces.button import Button


class ControlsInterface(InternalInterface):
    def __init__(self):
        buttons = pygame.sprite.Group([Button(150, 50, 'interfaces\Botoes\\botao_mainmenu_hover.png', 
                                                       'interfaces\Botoes\\botao_mainmenu.png',
                                                       'interfaces\Botoes\\botao_mainmenu_pressed.png', 'voltar')])
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaControles.png', buttons)

    def draw(self):
        self.getButtons().update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
