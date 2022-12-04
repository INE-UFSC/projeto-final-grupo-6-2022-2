from item import *
from levelBuilder import LevelBuilder
from debug import debug
from jogador import Jogador
from levelDAO import LevelDAO

class Level:
    def __init__(self):
        
        # Pegar a tela
        self.__lvl_builder = LevelBuilder()
        self.__dao = LevelDAO()
        self.__selected_room = 0
        self.display_surface = pygame.display.get_surface()
        self.__lvl_builder.create_map(self.__selected_room)
        self.__player = self.__lvl_builder.getPlayer()
        self.enemy_update()
        # Cria grupos de sprites

    def restart(self):
        self.__lvl_builder.create_map(self.__selected_room)
        self.__lvl_builder.getPlayer().loadInventory()
    
    def load(self):
        self.__selected_room = self.__dao.get('selected_room')
        self.__lvl_builder.create_map(self.__selected_room)
        self.__lvl_builder.getPlayer().loadInventory()
    
    def dump(self):
        self.__player.saveInventory()
        self.__dao.add(self)
        
    
    #RETIRAR ESSA FUNÇÂO DPS
    def getPlayerDead(self):
        if self.__player.getHealth() <= 0:
            return True
        return False

    def enemy_update(self):
        for enemy in self.__lvl_builder.getEnemySprites():
            enemy.light_info_update(self.__player.getPos(), self.__player.getLight().getStatus())
            enemy.update()

    def input(self):
        # Input de movimento
        # Se apertar J diminui a vida do player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.__player.tomar_Dano_ou_curar_vida(-1)
            print(self.__player.getHealth())
        if keys[pygame.K_k]:
            self.__player.tomar_Dano_ou_curar_vida(1)
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
        if keys[pygame.K_SPACE]:
            msg = self.__player.attack()
            if msg is not None:
                self.__lvl_builder.add_projectile(msg[0], msg[1], msg[2])
            self.__player.setAttackingStatus()

    def move_character(self):
        for character in list(self.__lvl_builder.getEnemySprites()) + [self.__player]:
            if character.getDirectionMagnitude() != 0:
                character.directionNormalize()
            character.hitbox.x += character.getDirectionX() * character.getSpeed()
            self.collision('horizontal', character) # passar colisao para level
            character.hitbox.y += character.getDirectionY() * character.getSpeed()
            self.collision('vertical', character) # passar colisao para level
            character.rect.center = character.hitbox.center

    def move_projectile(self):
        for proj in list(self.__lvl_builder.getProjectileSprites()):
            dirx, diry = proj.getDirection()
            speed = proj.getSpeed()
            if proj.getDirectionMagnitude() != 0:
                proj.directionNormalize()
            proj.hitbox.x += dirx * speed
            proj.hitbox.y += diry * speed
            self.projectile_collision(proj)
            proj.rect.center = proj.hitbox.center

    def projectile_collision(self, projectile):
        for sprite in self.__lvl_builder.getEnemySprites():
            if sprite.hitbox.colliderect(projectile.hitbox):
                projectile.hit(sprite)

        for sprite in self.__lvl_builder.getObstacleSprites():
            if sprite.hitbox.colliderect(projectile.hitbox):
                projectile.kill()

    def collision(self, direction, character):
        obstacle_sprites = list(self.__lvl_builder.getObstacleSprites())
        item_sprites = []

        if isinstance(character, Jogador):
            item_sprites = self.__lvl_builder.getItemSprites()
            enemy_sprites = self.__lvl_builder.getEnemySprites()

        else:
            enemy_sprites = [self.__player]

        if direction == 'horizontal':
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(character.hitbox):
                    if character.getDirectionX() > 0:  # Se mover para a direita
                        character.hitbox.right = sprite.hitbox.left  # left
                    if character.getDirectionX() < 0:  # Se mover para a esquerda
                        character.hitbox.left = sprite.hitbox.right  # right

            for sprite in enemy_sprites:
                if sprite.hitbox.colliderect(character.hitbox):
                    if character.getDirectionX() > 0:  # Se mover para a direita
                        character.hitbox.right = sprite.hitbox.left  # left
                    if character.getDirectionX() < 0:  # Se mover para a esquerda
                        character.hitbox.left = sprite.hitbox.right  # right

            for item in item_sprites:
                if item.hitbox.colliderect(character.hitbox):
                    add = character.getInventory().add_item(item)
                    if add:
                        item_sprites.remove(item)
                        item.exclui()

        if direction == 'vertical':
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(character.hitbox):
                    if character.getDirectionY() > 0:  # Se mover para baixo
                        character.hitbox.bottom = sprite.hitbox.top  # top
                    if character.getDirectionY() < 0:  # Se mover para cima
                        character.hitbox.top = sprite.hitbox.bottom  # bottom

            for sprite in enemy_sprites:
                if sprite.hitbox.colliderect(character.hitbox):
                    if character.getDirectionY() > 0:  # Se mover para baixo
                        character.hitbox.bottom = sprite.hitbox.top  # top
                    if character.getDirectionY() < 0:  # Se mover para cima
                        character.hitbox.top = sprite.hitbox.bottom  # bottom

            for item in item_sprites:
                if item.hitbox.colliderect(character.hitbox):
                    add = character.getInventory().add_item(item)
                    if add:
                        item_sprites.remove(item)
                        item.exclui()

    def run(self):
        # Atualizar e desenhar sprites/jogo
        self.enemy_update()
        self.__player = self.__lvl_builder.getPlayer()
        self.input()
        self.__lvl_builder.getVisibleSprites().custom_draw(self.__player)
        self.__player.draw()
        self.__lvl_builder.getVisibleSprites().update()
        self.move_character()
        self.move_projectile()
        self.chave()
        self.draw_hud()
        
        debug('Sala', self.__selected_room, 100, 20)


    def draw_hud(self):
        self.__lvl_builder.getHud().draw(self.__player)

        
    def chave(self):
        inventario = self.__player.getInventory().getItemList()
        if self.__lvl_builder.getKey() in inventario:
            inventario.remove(self.__lvl_builder.getKey())
            inventario.append(None)
            self.__lvl_builder.getObstacleSprites().remove(self.__lvl_builder.getDoor())
        if self.__lvl_builder.getDoor() in inventario:
            inventario.remove(self.__lvl_builder.getDoor())
            inventario.append(None)
            self.__selected_room += 1
            self.dump()
            self.load()

    def getPlayer(self):
        return self.__player
    
    def getSelectRoom(self):
        return self.__selected_room
