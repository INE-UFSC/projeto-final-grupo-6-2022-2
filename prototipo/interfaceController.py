from ingame import InGame
from interfaces.menuInterface import MenuInterface
from interfaces.gameoverInterface import GameOverInterface
from interfaces.pauseInterface import PauseInterface
from interfaces.optionsInterface import OptionsInterface
from interfaces.controlsInterface import ControlsInterface

class InterfaceController:
    def __init__(self):
        self.__ingame = InGame()
        self.__mainmenu = MenuInterface()
        self.__pause = PauseInterface()
        self.__options = OptionsInterface()
        self.__controls = ControlsInterface()
        self.__gameover = GameOverInterface()
        self.__last_screen = None

    def firstInterface(self):
        return self.__mainmenu
    
    def nextInterface(self, key, screen):
        
        if key == 'mainmenu':
            return self.__mainmenu
        elif key == 'start':
            self.__ingame = InGame()
            return self.__ingame
        elif key == 'continue':
            if isinstance(screen, PauseInterface):
                return self.__ingame
            else:
                self.__ingame.loadgame()
                return self.__ingame
        elif key == 'morreu':
            return self.__gameover
        elif key == 'pause':
            return self.__pause 
        elif key == 'restart':
            self.__ingame.level.restart()
            return self.__ingame
        elif key == 'options':
            self.__last_screen = screen
            return self.__options
        elif key == 'controls':
            return self.__controls
        elif key == 'voltar':
            return self.__last_screen