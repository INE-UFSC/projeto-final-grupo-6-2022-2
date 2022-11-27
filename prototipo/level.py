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
        self.enemy_update()

        # Cria grupos de sprites

    def enemy_update(self):
        for enemy in self.__lvl_builder.getEnemySprites():
            enemy.light_info_update(self.__player.getPos(), self.__player.getLight().getStatus())
            enemy.update()

    def input(self):
        # Input de movimento
        # Se apertar J diminui a vida do player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.__player.setHealth(self.__player.getHealth() - 1)
            print(self.__player.getHealth())
        if keys[pygame.K_k]:
            self.__player.setHealth(self.__player.getHealth() + 1)
            print(self.__player.getHealth())

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

    def move_character(self):
        for character in list(self.__lvl_builder.getEnemySprites()) + [self.__player]:
            if character.getDirectionMagnitude() != 0:
                character.directionNormalize()
            character.hitbox.x += character.getDirectionX() * character.getSpeed()
            character.collision('horizontal') # passar colisao para level
            character.hitbox.y += character.getDirectionY() * character.getSpeed()
            character.collision('vertical') # passar colisao para level
            character.rect.center = character.hitbox.center

    def run(self):
        # Atualizar e desenhar sprites/jogo
        self.input()
        self.__lvl_builder.getVisibleSprites().custom_draw(self.__player)
        self.__player.draw()
        self.__lvl_builder.getVisibleSprites().update()
        self.enemy_update()
        self.move_character()
        self.chave()
        self.draw_hud()
        
        debug('Sala', self.__selected_room, 100, 20)


    def draw_hud(self):
        self.__lvl_builder.getHud().draw(self.__player)

        
    def chave(self):
        inventario = self.__player.getInventory().getItemList()
        if self.__lvl_builder.getKey() in inventario:
            inventario.remove(self.__lvl_builder.getKey())
            self.__lvl_builder.getObstacleSprites().remove(self.__lvl_builder.getDoor())
        if self.__lvl_builder.getDoor() in inventario:
            inventario.remove(self.__lvl_builder.getDoor())
            self.__selected_room += 1
            self.__lvl_builder.create_map(self.__selected_room)
            

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
