import pygame


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        # Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()
        self.chao = pygame.image.load('tiles/chao.png').convert_alpha()
        self.chao_rect = self.chao.get_rect(topleft = (0,0))

    def custom_draw(self, jogador):
        # Pegando offset
        self.offset.x = jogador.rect.centerx - self.half_width
        self.offset.y = jogador.rect.centery - self.half_height
        self.chao_pos = self.chao_rect.topleft - self.offset
        self.display_surface.blit(self.chao, self.chao_pos)
        # Desenhando sprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
