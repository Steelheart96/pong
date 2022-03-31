from pyray import Color, draw_text
from Structs import Point


class TextOverlay:
    '''
    Description: The text for the Overlay instance(s).

    Args:
    - text (str): The text the TextOverlay instance will be displaying
    - font_size (int): The size of the text the TextOverlay instance will be displaying
    - color (pr.Color): The color of the text the TextOverlay instance will be displaying
    - position (Point): The position of the text the TextOverlay instance will be displaying
    '''

    def __init__(self, text: str, font_size:int, color: Color, position: Point) -> None:
        self._text = text
        self._font_size = font_size
        self._color = color
        self._position = position

    def draw(self):
        '''
        Description: Draws TextOverlay instance onto the screen.
        '''
        draw_text(self._text, self._position.x_pos, self._position.y_pos, self._font_size, self._color)