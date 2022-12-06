from ingame import InGame
from interfaces.menuScreen import MenuScreen
from interfaces.gameoverScreen import GameOverScreen
from interfaces.pauseScreen import PauseScreen
from interfaces.optionsScreen import OptionsScreen
from interfaces.controlsScreen import ControlsScreen

class ScreenController:
    def __init__(self):
        self.__ingame = InGame()
        self.__mainmenu = MenuScreen()
        self.__pause = PauseScreen()
        self.__options = OptionsScreen()
        self.__controls = ControlsScreen()
        self.__gameover = GameOverScreen()
        self.__last_screen = None

    def firstScreen(self):
        return self.__mainmenu
    
    def nextScreen(self, key, screen):
        
        if key == 'mainmenu':
            return self.__mainmenu
        elif key == 'start':
            self.__ingame = InGame()
            return self.__ingame
        elif key == 'continue':
            if isinstance(screen, PauseScreen):
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