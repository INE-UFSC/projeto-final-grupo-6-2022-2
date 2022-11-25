import pygame

class Sound:
    def __init__(self, filename):
        self.filename = filename
        self.sound = pygame.mixer.Sound('sounds/' + filename + '.wav')
        self.sound.set_volume(0.1)
        
    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()
