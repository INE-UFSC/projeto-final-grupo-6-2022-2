import pygame

from pilha import Pilha
from settings import WIDTH, HEIGTH
from sound import Sound


class Lanterna(pygame.sprite.Sprite):
    def __init__(self, pos, status=False, tempo_ligada=0):
        super().__init__(pygame.sprite.Group())
        self.__som = Sound('lanterna')
        self.cor = (0, 255, 255)
        self.__status = status
        self.pilha = Pilha(pos[0], pos[1], 'tiles/pilha.png', 50)
        self.tempo_ligada = tempo_ligada

        self.image = pygame.image.load('tiles/light.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.__x = (WIDTH - self.rect[2]) / 2
        self.__y = (HEIGTH - self.rect[3]) / 2
        # self.hitbox = self.rect.inflate(0,-26)

        self.__toggle_timer = 0  # timer para impedir que a pilha fique ligando ou desligando se o jogador segurar CTRL
        self.__toggle_cooldown = 2

    def cooldown(self):
        if self.__toggle_timer > 0:
            self.__toggle_timer -= 1

    def update(self):
        self.cooldown()
        self.pilha.contador()

    def setPos(self, x, y):
        self.hitbox.x = x
        self.hitbox.y = y

    def setPilha(self, pilha: Pilha):
        self.pilha = pilha
        self.pilha.setUsando(self.__status)

    def setHealth(self, health):
        self.health = health

    def getStatus(self):
        return self.__status

    def setStatus(self):
        # o toggle_timer impede que a lanterna fique desligando e ligando rapidamente
        # caso o jogador segure CTRL
        if self.__toggle_timer <= 0:
            self.__status = not self.__status
            self.__som.play()
            self.pilha.setUsando(self.__status)

        self.__toggle_timer = self.__toggle_cooldown

    def draw(self, tela):
        if self.__status and self.pilha.getUsando() and self.pilha.getStatus():
            tela.blit(self.image, (self.__x, self.__y))
        else:
            pygame.draw.rect(tela, (0, 0, 0), (0, 0, WIDTH, HEIGTH))
