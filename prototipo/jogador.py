import pygame

class Jogador:
    def init(self, x, y, cor, tamanho: list, pilha: list):
        self.x = x
        self.y = y
        self.cor = cor
        self.tamanho = tamanho
        self.pilha = pilha
        
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.tamanho[0], self.tamanho[1]))

    def movimentar(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 0.5
        if keys[pygame.K_RIGHT]:
            self.x += 0.5
        if keys[pygame.K_UP]:
            self.y -= 0.5
        if keys[pygame.K_DOWN]:
            self.y += 0.5
        #Movimentação do jogador está diferente na diagonal do que na horizontal e vertical (0.5 e 0.7)
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            #Ainda está muito rápido
            self.x -= 0.05
            self.y -= 0.05
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.x -= 0.05
            self.y += 0.05
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.x += 0.05
            self.y -= 0.05
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.x += 0.05
            self.y += 0.05