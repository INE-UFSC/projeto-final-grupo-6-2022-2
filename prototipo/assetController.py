import pygame
from singletonMeta import SingletonMeta


class AssetController(metaclass=SingletonMeta):

    def __init__(self):
        self.__assets = {'player': pygame.image.load('tiles/player.png').convert_alpha(),
                         'hud_vida': pygame.image.load('tiles/hud_vida.png').convert_alpha(),
                         'inventario': pygame.image.load('tiles/inventario.png').convert_alpha(),
                         'parede_vertical_esquerda': pygame.image.load('tiles/parede_vertical_esquerda.png').convert_alpha(),
                         'parede_quina_direita_cima': pygame.image.load('tiles/parede_quina_direita_cima.png').convert_alpha(),
                         'parede_quina_esquerda_baixo': pygame.image.load('tiles/parede_quina_esquerda_baixo.png'),
                         'parede_quina_direita_baixo': pygame.image.load('tiles/parede_quina_direita_baixo.png').convert_alpha(),
                         'parede_quina_esquerda_cima': pygame.image.load('tiles/parede_quina_esquerda_cima.png').convert_alpha(),
                         'parede': pygame.image.load('tiles/parede.png').convert_alpha(),
                         'parede_com_corrente': pygame.image.load('tiles/parede_com_corrente.png').convert_alpha(),
                         'parede_com_vaso': pygame.image.load('tiles/parede_com_vaso.png').convert_alpha(),
                         'parede_vertical_direita': pygame.image.load('tiles/parede_vertical_direita.png').convert_alpha(),
                         'parede_horizontal_cima': pygame.image.load('tiles/parede_horizontal_cima.png').convert_alpha(),
                         'pilha': pygame.image.load('tiles/pilha.png').convert_alpha(),
                         'hud_pilha': pygame.image.load('tiles/hud_pilha.png').convert_alpha(),
                         'porta': pygame.image.load('tiles/porta.png').convert_alpha(),
                         'barril': pygame.image.load('tiles/barril.png').convert_alpha(),
                         'porta_cima': pygame.image.load('tiles/porta_cima.png').convert_alpha(),
                         'key': pygame.image.load('tiles/key.png'),
                         'key_indisponivel': pygame.image.load('tiles/key_indisponivel.png'),
                         'enemyhighdmg': pygame.image.load('tiles/parede_vertical_direita.png').convert_alpha(),
                         'enemylowdmg': pygame.image.load('tiles/porta.png').convert_alpha()
                         }

    def get_asset(self, key):
        try:
            return self.__assets[key]
        except KeyError:
            print('Asset não encontrada: ' + key)
            return None
