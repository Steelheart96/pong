from Structs import Window
from Director.Credits import Credits
from Director.Menu import Menu
from Director.GamePlay import GamePlay
import pyray as pr

class Director:
    '''
    Description: Creates and controls all main game logic.

    Args:
    - window (Window): Information about the window
    - player_keys (dict): The player keys to look for input from ("input type": "outcome")
    '''

    def __init__(self, window: Window, player_keys: dict) -> None:
        self.window = window
        self.player_keys = player_keys
        self.initialize_window()
        self.credits = Credits(window, self)
        self.menu = Menu(window, self)
        self.gameplay = GamePlay(window, player_keys, self)
        self.playing_menu = True
        self.playing_credits = False
        self.playing_game = False

    def initialize_window(self):
        '''
        Description: Initializes pyray program window.
        '''
        pr.init_window(self.window.width, self.window.height, self.window.caption)
        pr.set_target_fps(self.window.fps_cap)

    def run(self):
        '''
        Description: Runs the program loop.
        '''
        run = True
        while run:
            if self.playing_menu:
                run = self.menu.run()

            if self.playing_game:
                run = self.gameplay.run()
            
            if self.playing_credits:
                run = self.credits.run()
        
    def close(self):
        '''
        Description: Closes pyray program window.
        '''
        pr.close_window()