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
    
    def firstInterface(self):
        return self.__mainmenu
    
    def nextInterface(self, key, running):
        if key == 'mainmenu':
            return self.__mainmenu, False
        elif key == 'start' or key == 'continue':
            return InGame(), True
        elif key == 'morreu':
            return self.__gameover, False
        elif key == 'pause':
            return self.__pause, True  
        elif key == 'restart':
            self.__ingame.level.restart()
            return self.__ingame, True
        elif key == 'options':
            return self.__options, running
        elif key == 'controls':
            return self.__controls, running
        elif key == 'voltar':
            if running:
                return self.__pause, True
            else:
                return self.__mainmenu, False