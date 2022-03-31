from Structs import Dimensions, Point
from pyray import Color, draw_rectangle

class BackgroundOverlay:
    '''
    Description: The background for the Overlay instance(s).

    Args:
    - dimentions (Dimensions): The width and height of the overlay
    - position (Point): The position of the overrlay's top right corner on the screen
    - color (pr.Color): The color of the overlay
    - screen_side (str): The side of the screen that the Menu Overlay will be drawn on
    - window_width (int): The width of the program window
    '''

    def __init__(self, dimensions: Dimensions, color: Color, screen_side: str, window_width: int) -> None:
        self._dimensions = dimensions
        self.color = color
        self._screen_side = screen_side
        self.window_width = window_width
        self.set_position()

    def set_position(self):
        '''
        Description: Positions BackgroundOverlay instance on screen.
        '''
        if self._screen_side == 'left':
            x_pos = 0
        else:
            x_pos = self.window_width // 2
        y_pos = 0

        self._position = Point(x_pos, y_pos)

    def draw(self):
        '''
        Description: Draws BackgroundOverlay instance onto the screen.
        '''
        draw_rectangle(
                self._position.x_pos,
                self._position.y_pos,
                self._dimensions.width,
                self._dimensions.height,
                self.color
            )