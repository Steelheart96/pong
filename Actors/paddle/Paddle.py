from Actors.Actor import Actor
from Structs.Window import Window
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

    def __init__(self, window: Window, texture: pr.Texture, paddle_side: str):
        super().__init__(window)
        self.texture = texture
        self.paddle_side = paddle_side.lower()
        self.set_start_position()

    def update_position(self, y_pos: int):
        '''
        Description: Paddle update coordinate function.

        Args:
        y_pos (int): y position update     
        '''
        self.position_y += y_pos

    def set_start_position(self):
        '''
        Description: Sets the start position of the paddle.
        '''
        if self.paddle_side == 'left':
            self.position_x = self.window.width // 8

        if self.paddle_side == 'right':
            self.position_x = self.window.width // 8 * 7

        self.position_y = self.window.height // 2 - self.texture.width // 2

    def draw(self):
        '''
        Description: Draws the paddle onto the screen.
        '''
        pr.draw_texture_rec(
            self.texture,
            pr.Rectangle(0,0, float(self.texture.width), float(self.texture.height)),
            pr.Vector2(self.position_x, self.position_y),
            pr.WHITE)