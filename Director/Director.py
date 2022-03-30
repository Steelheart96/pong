from Structs import Window
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
        self.gameplay = GamePlay(window, player_keys)

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
        self.gameplay.run()
        
    def close(self):
        '''
        Description: Closes pyray program window.
        '''
        pr.close_window()