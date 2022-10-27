import pygame

#Deve ser uma classe Abstrata
class Item(pygame.sprite.Sprite):
    def  __init__(self, x, y, sprite,grupo):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(grupo)
        self.x = x
        self.y = y
        self.sprite = sprite
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.hitbox = self.rect.inflate(0,0)
        self.posicao = [self.x, self.y]
    
    def usar(self):
        #Só teste. Essa funcão aqui deve ser um abstract method
        print("usado")
        self.kill()
        
    def exclui(self):
        
        self.kill()

    def draw(self, x, y, valor, pos, surface):
        surface.blit(self.image, (valor*pos+x, y-4))