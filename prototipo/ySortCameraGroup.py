import pygame


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        # Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

    

    def custom_draw(self, jogador):
        # Pegando offset
        self.offset.x = jogador.getRect().centerx - self.half_width
        self.offset.y = jogador.getRect().centery - self.half_height
        # Desenhando sprites
        for sprite in self.sprites():
            offset_pos = sprite.getRect().topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
