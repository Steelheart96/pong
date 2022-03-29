from Actors.Actor import Actor
from Structs import Dimensions, Point, Window
import pyray as pr

class Paddle(Actor):
    '''
    Description: Class for creating and managing the paddles.

    Args:
    - window (Window): The programs information about the Window
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    - texture (pr.Texture): The texture of the paddle
    '''

    def __init__(self, window: Window, dimensions: Dimensions, color: pr.Color, paddle_side: str):
        super().__init__(window)
        self.dimensions = dimensions
        self.color = color
        self._width = dimensions.width
        self._height = dimensions.height
        self._paddle_side = paddle_side.lower()
        self.set_start_position()

    def update_position(self, y_pos: int):
        '''
        Description: Paddle update coordinate function.

        Args:
        y_pos (int): y position update     
        '''
        self._position.y_pos += y_pos

    def set_start_position(self):
        '''
        Description: Sets the start position of the paddle.
        '''
        if self._paddle_side == 'left':
            position_x = self.window.width // 8

        if self._paddle_side == 'right':
            position_x = self.window.width // 8 * 7

        position_y = self.window.height // 2 - self._width // 2

        self._position = Point(position_x, position_y)

    def reset(self):
        '''
        Description: Resets the Paddle instances position.
        '''
        self.set_start_position()

    def draw(self):
        '''
        Description: Draws the paddle onto the screen.
        '''
        pr.draw_rectangle(self._position.x_pos, self._position.y_pos, self._width, self._height, self.color)
    
    def get_width(self):
        '''
        Description: Gets Paddle instance width.
        '''
        return self._width

    def get_height(self):
        '''
        Description: Gets Paddle instance height.
        '''
        return self._height

    def get_position(self):
        '''
        Description: Gets Paddle instance position.
        '''
        return self._position