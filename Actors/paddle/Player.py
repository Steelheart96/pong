import pyray as pr
from Actors.paddle.Paddle import Paddle
from Movement.Input import Input
from Structs import Dimensions, Window

class Player(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    '''
    def __init__(self, window: Window, dimensions: Dimensions, color: pr.Color, paddle_side: str, player_input: Input):
        super().__init__(window, dimensions, color, paddle_side)
        self.input = player_input

    def get_y_position(self):
        return self.input.process(self._position.y_pos, self._height)
    
    def update_position(self, y_pos: int):
        '''
        Description: Paddle update coordinate function.

        Args:
        y_pos (int): y position update     
        '''
        self._position.y_pos += y_pos