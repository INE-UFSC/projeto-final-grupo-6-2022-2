import pygame
import jogador
import lanterna
import pilha
from jogador import Jogador
from lanterna import Lanterna
from pilha import Pilha
from pygame.locals import *
from item import Item


tela = pygame.display.set_mode((800, 600))
pygame.init()
jogador = Jogador()
jogador.init(100, 100, (255, 0, 0), (50, 50), [])
lanterna = Lanterna(100, 100, (255, 255, 255), (50, 50))
pilha = Pilha(100)
clock = pygame.time.Clock()
item = Item(200, 200, (50, 50), (0, 255, 0), "pilha")


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pilha.tempo_restante > 0:
                    lanterna.status = not lanterna.status
                else:
                    print('sem pilha')

    if lanterna.status:
        lanterna.tempo_ligada += 1    
        print(lanterna.tempo_ligada)
    if lanterna.tempo_ligada > 60:
        pilha.tempo_restante -= 1
        lanterna.tempo_ligada = 0
        if pilha.tempo_restante == 0:
            lanterna.status = False
            print(pilha.tempo_restante)

        
             

    tela.fill((0, 0, 0))
    jogador.desenhar(tela)
    #lanterna.lanterna(tela)Z
    jogador.movimentar()
    pilha.draw_timer(tela)
    pygame.display.update()
    item.spawnar_item(tela)
    item.pegar_item(jogador)
