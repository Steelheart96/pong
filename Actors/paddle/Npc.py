from Actors.paddle.Paddle import Paddle
from Structs import Window, Dimensions
import pyray as pr
from Actors.ball.Ball import Ball

class npc(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - dimensions (Dimensions): Width and Height of paddle
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right')
    - ball (Ball): The ball Actor currently on screen
    - top_bottom_wall_height (int): The top window Wall height
    '''

    def __init__(self, window: Window, dimensions: Dimensions, color: pr.Color, paddle_side: str, ball: Ball, top_bottom_wall_height: int):
        super().__init__(window, dimensions, color, paddle_side)
        self.ball = ball
        self.top_bottom_wall_height = top_bottom_wall_height

    def get_y_position(self):
        '''
        Description: Locates Ball actor's y position.
        '''
        return self.ball.get_pos_y()

    def update_position(self, y_pos: int):
        '''
        Description: Sets Paddle y location to ball y location.

        Args:
        y_pos (int): y position update  
        '''
        self._new_pos_y = y_pos - (self._height // 2)

        if self.top_bottom_wall_height < self._new_pos_y < self.window.height - self.top_bottom_wall_height - self._height:
            self._position.y_pos = self._new_pos_y