import pyray as pr
from Actors.paddle.Paddle import Paddle
from Structs.Window import Window

class Player(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    '''
    def __init__(self, window: Window, texture: pr.Texture, paddle_side: str):
        super().__init__(window, texture, paddle_side)