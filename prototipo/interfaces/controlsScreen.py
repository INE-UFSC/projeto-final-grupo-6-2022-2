import pygame

from interfaces.abstractScreen import AbstractScreen
from interfaces.button import Button


class ControlsScreen(AbstractScreen):
    def __init__(self):
        buttons = pygame.sprite.Group([Button(150, 50, 'interfaces\Botoes\\botao_mainmenu_hover.png', 
                                                       'interfaces\Botoes\\botao_mainmenu.png',
                                                       'interfaces\Botoes\\botao_mainmenu_pressed.png', 'mainmenu')])
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaControles.png', buttons)

    def update(self):
        self.getButtons().update()
        
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
