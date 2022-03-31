from typing import Any
from Structs import Point, Dimensions
import pyray as pr

class ButtonOverlay:
    '''
    Description: The button for the Overlay instance(s).

    Args:
    - text (str): The text that will be on the button
    - text_color (pr.Color): The color that the text on the button will be
    - position (Point): The position of the ButtonOverlay instance on the screen
    - dimensions (Dimensions): The width and height of the ButtonOverlay instance
    - background_color (pr.Color): The background color of the ButtonOverlay instance
    - func_on_click (function): The function that runs when the button is clicked
    '''
    def __init__(self, text: str, text_color: pr.Color, position: Point, dimensions: Dimensions, background_color: pr.Color, func_on_click: Any) -> None:
        self._text = text
        self._text_color = text_color
        self._rec_position = position
        self._dimensions = dimensions
        self._background_color = background_color
        self._func_on_click = func_on_click
        self.calculate_text_position()
    
    def draw(self):
        '''
        Description: Draws the ButtonOverlay instance on the screen.
        '''
        self.draw_background()
        self.draw_text()

    def draw_background(self):
        '''
        Description: Draws the background rectangle of the ButtonOverlay instance.
        '''
        pr.draw_rectangle(
                self._rec_position.x_pos,
                self._rec_position.y_pos,
                self._dimensions.width,
                self._dimensions.height,
                self._background_color
            )

    def draw_text(self):
        '''
        Description: Draws the text of the ButtonOverlay instance.
        '''
        pr.draw_text(
                self._text,
                self._text_position.x_pos,
                self._text_position.y_pos,
                self._font_size,
                self._text_color
            )

    def calculate_text_font_size(self):
        '''
        Description: Calculates the text font size for the text inside the ButtonOverlay instance.
        '''
        self._font_size = self._dimensions.height // 2
        # self._font_size = 12

    def calculate_text_length(self):
        '''
        Description: Calculates the text length for the text inside the ButtonOverlay instance.
        '''
        self._text_length = pr.text_length(self._text)

    def calculate_text_position(self):
        '''
        Description: Calculates the text position inside the ButtonOverlay instance.
        '''
        self.calculate_text_length()
        self.calculate_text_font_size()

        self._text_position = Point(
                x_pos = self._rec_position.x_pos + (self._dimensions.width // 2) - (self._text_length * self._font_size // 4),
                y_pos = self._rec_position.y_pos + (self._dimensions.height // 2) - (self._font_size // 2)
            )

    def input_check(self):
        '''
        Description: Checks for a mouse click and executes func_on_click.
        '''
        if self.mouse_over():
            if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
                self._func_on_click()

    def mouse_over(self):
        '''
        Description: Checks to see if the mouse is over the button. 
        '''
        mouse_position = pr.get_mouse_position()
        return pr.check_collision_point_rec(
                pr.Vector2(
                    mouse_position.x,
                    mouse_position.y
                    ),
                pr.Rectangle(
                    self._rec_position.x_pos,
                    self._rec_position.y_pos,
                    self._dimensions.width,
                    self._dimensions.height
                )
            )