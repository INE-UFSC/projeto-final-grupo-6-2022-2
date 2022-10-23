import pygame

class Pilha:
    def __init__(self, nivel, acabou = False, usando = False, tempo_restante = 10, tamanho = [100, 20], x = 0, y = 0):
        super(Pilha, self).__init__()
        self.image = pygame.image.load("tiles/pilha.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nivel = nivel
        self.acabou = acabou
        self.usando = usando
        self.tempo_restante = tempo_restante
        self.tamanho = tamanho
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw_timer(self, tela):
        pygame.draw.rect(tela, (0, 0, 255), (self.x + 10, self.y, self.tamanho[0], self.tamanho[1]))
        pygame.draw.rect(tela, (0, 255, 0), (self.x + 10, self.y, self.tamanho[0] * (self.tempo_restante / 10), self.tamanho[1]))
        pygame.draw.rect(tela, (255, 0, 0), (self.x + 10, self.y, self.tamanho[0] * (self.tempo_restante / 10), self.tamanho[1]), 1)
