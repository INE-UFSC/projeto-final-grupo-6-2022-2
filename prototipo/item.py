import pygame



class Item:
    def  __init__(self, x, y, tamanho, cor, tipo):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = cor
        self.tipo = tipo
    
    def spawnar_item(self, tela):
        pygame.draw.rect(tela, self.cor, (100, 200, self.tamanho[0], self.tamanho[1]))
        
    
    def pegar_item(self, jogador):
        if jogador.x == self.x and jogador.y == self.y:
            if self.tipo == "pilha":
                self.pilha.tempo_restante += 10
                self.x = 0
                self.y = 0
        