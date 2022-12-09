import pygame
from singletonMeta import SingletonMeta
# class Sound:
#     def __init__(self, filename):
#         self.filename = filename
#         self.sound = pygame.mixer.Sound('sounds/' + filename + '.wav')
#         self.sound.set_volume(0.1)
#
#     def play(self):
#         self.sound.play()
#
#     def stop(self):
#         self.sound.stop()


class Sound(metaclass=SingletonMeta):

    def __init__(self):
        self.__current_requestor = None
        self.__music = pygame.mixer.music
        self.__music_priority = 0
        self.__sound_channel = pygame.mixer.Channel(1)
        self.__sounds = {'pilha': pygame.mixer.Sound('sounds/pilha.wav'),
                         'sem_pilha': pygame.mixer.Sound('sounds/sem_pilha.wav'),
                         'key': pygame.mixer.Sound('sounds/key.wav'),
                         'lanterna': pygame.mixer.Sound('sounds/lanterna.wav')}
        self.__songs = {}
        self.__priorities = {}


    def playSound(self, sound_name):
        self.__sound_channel.play(self.__sounds[sound_name])

    def stopSound(self):
        if self.__sound_channel.get_busy():
            self.__sound_channel.stop()

    def playMusic(self, requestor):
        try:
            if not self.__music.get_busy():
                self.__music.unload()
                self.__music.load(self.__songs[requestor])
                self.__music.play()
            elif self.__priorities[requestor] >= self.__music_priority:
                self.__music.fadeout(2000)
                self.__music.unload()
                self.__music.load(self.__songs[requestor])
                self.__music.play(loops=-1)

                self.__music_priority = self.__priorities[requestor]
        except KeyError:
            print('Chave Invalida!')
            return 0
        self.__current_requestor = requestor

    def stopMusic(self, requestor):
        if requestor == self.__current_requestor:
            self.__music.stop()

    def setVolume(self, volume: float):
        self.__music.set_volume(volume/200)
        self.__sound_channel.set_volume(volume/100)
