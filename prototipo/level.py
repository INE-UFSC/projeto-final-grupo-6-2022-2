from item import *
from levelBuilder import LevelBuilder
from debug import debug


class Level:
    def __init__(self):
        
        # Pegar a tela
        self.__lvl_builder = LevelBuilder()
        self.__selected_room = 0
        self.display_surface = pygame.display.get_surface()
        self.__lvl_builder.create_map(self.__selected_room)
        self.__player = self.__lvl_builder.getPlayer()
        # Cria grupos de sprites

    def run(self):
        # Atualizar e desenhar sprites/jogo
        self.input()
        self.__lvl_builder.getVisibleSprites().custom_draw(self.__player)
        self.__player.draw()
        self.__lvl_builder.getVisibleSprites().update()
        self.__lvl_builder.getEnemySprites().update()
        self.chave()
        self.draw_hud()
        
        debug('Sala', self.__selected_room, 100, 20)

    def draw_hud(self):
        self.__lvl_builder.getHud().draw(self.__player.getLight().pilha)
        
        
    def chave(self):
        inventario = self.__player.getInventory().getItemList()
        if self.__lvl_builder.getKey() in inventario:
            inventario.remove(self.__lvl_builder.getKey())
            self.__lvl_builder.getObstacleSprites().remove(self.__lvl_builder.getDoor())
        if self.__lvl_builder.getDoor() in inventario:
            inventario.remove(self.__lvl_builder.getDoor())
            self.__selected_room += 1
            self.__lvl_builder.create_map(self.__selected_room)

    def input(self):
        # Input de movimento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.__player.setDirectionY(-1)
            self.__player.setStatus('up')
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.__player.setDirectionY(1)
            self.__player.setStatus('down')
        else:
            self.__player.setDirectionY(0)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.__player.setDirectionX(1)
            self.__player.setStatus('right')
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.__player.setDirectionX(-1)
            self.__player.setStatus('left')
        else:
            self.__player.setDirectionX(0)

        # Input de inventário
        if keys[pygame.K_1]:
            self.__player.getInventory().use_item(1, self.__player)
        elif keys[pygame.K_2]:
            self.__player.getInventory().use_item(2, self.__player)
        elif keys[pygame.K_3]:
            self.__player.getInventory().use_item(3, self.__player)
        elif keys[pygame.K_4]:
            self.__player.getInventory().use_item(4, self.__player)
        elif keys[pygame.K_5]:
            self.__player.getInventory().use_item(5, self.__player)
        elif keys[pygame.K_6]:
            self.__player.getInventory().use_item(6, self.__player)
        elif keys[pygame.K_7]:
            self.__player.getInventory().use_item(7, self.__player)
        elif keys[pygame.K_8]:
            self.__player.getInventory().use_item(8, self.__player)
        elif keys[pygame.K_9]:
            self.__player.getInventory().use_item(9, self.__player)

        if keys[pygame.K_LCTRL]:
            self.__player.getLight().setStatus()

        # Input de ataques
        if keys[pygame.K_SPACE] and not self.__player.getAttackingStatus():
            self.__player.setAttackingStatus()
            self.__player.setAttackTimer()
            self.__player.attack()


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
        self.offset.x = jogador.rect.centerx - self.half_width
        self.offset.y = jogador.rect.centery - self.half_height
        # Desenhando sprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
