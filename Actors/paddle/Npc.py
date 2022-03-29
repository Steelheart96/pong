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
    - top_wall_height (int): The top window Wall height
    - bottom_wall_height (int): The bottom window Wall height
    '''

    def __init__(self, window: Window, dimensions: Dimensions, color: pr.Color, paddle_side: str, ball: Ball, top_wall_height: int, bottom_wall_height: int):
        super().__init__(window, dimensions, color, paddle_side)
        self.ball = ball
        self._top_wall_height = top_wall_height
        self._bottom_wall_height = bottom_wall_height

    def locate_ball_y(self):
        '''
        Description: Locates Ball actor's y position.
        '''
        return self.ball.get_pos_y()

    def set_location(self):
        '''
        Description: Sets Paddle y location to ball y location.
        '''

        self._new_pos_y = self.locate_ball_y() - (self._height // 2)

        if self._top_wall_height < self._new_pos_y < self.window.height - self._bottom_wall_height - self._height:
            self._position.y_pos = self._new_pos_y