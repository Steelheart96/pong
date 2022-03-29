import pyray as pr
from Structs import Point

class Wall:
    '''
    Description: A class for creating and managing walls.

    Args:
    - width (int): width of the wall
    - height (int): height of the wall
    - pos_x (int): x position of the wall
    - pos_y (int): y position of the wall
    - color (pr.Color): color of the wall 
    '''

    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, color: pr.Color) -> None:
        self._width = width
        self._height = height
        self._position = Point(pos_x, pos_y)
        self.color = color

    def get_width(self):
        '''
        Description: Gets Window instance width.
        '''
        return self._width

    def get_height(self):
        '''
        Description: Gets Window instance height.
        '''
        return self._height

    def get_position(self):
        '''
        Description: Gets Wall instance position.
        '''
        return self._position

    def draw(self):
        '''
        Description: Draws wall instance.
        '''
        pr.draw_rectangle(self._position.x_pos, self._position.y_pos, self._width, self._height, self.color)