import pyray as pr
from Actors.ball.Ball import Ball
from StaticObjects.Wall import Wall
from Structs import Window, Point

class Score:
    '''
    Description: Creates and manages paddle scores.
    
    Args: 
    - window (Window): The program window attributes
    - wall (Wall): The wall instance that the score instance monitors
    - ball (Ball): The ball instance that will be watched for colissions
    - monitor_side (str): The paddle's side that the score is tracking ('left', 'right')
    - font_size (int): The font size the score text will be
    - color (pr.Color): The color the font will be
    '''

    def __init__(self, window: Window, wall:Wall, ball: Ball, monitor_side: str, font_size: int, color: pr.Color) -> None:
        self.window = window
        self.wall = wall
        self.ball = ball
        self._monitor_side = monitor_side
        self._font_size = font_size
        self._color = color
        self._paddle_score = 0
        self.set_position()

    def set_position(self):
        '''
        Description: Sets the position of the score.
        '''
        if self._monitor_side == "left":
            pos_x = self.window.width // 4
        else:
            pos_x = (self.window.width // 4) * 3

        pos_y = self.window.height // 3 * 2

        self._position = Point(pos_x, pos_y)

    def update(self):
        '''
        Description: Adds 1 point to the Paddle's score.
        '''
        if self.check_wall_collision():
            self._paddle_score += 1

    def check_wall_collision(self):
        '''
        Description: Checks to see what wall was hit by the ball.

        Returs:
        - Bool: True ball collided with tracked wall | False Ball did not collide with tracked wall
        '''
        return self.ball.check_collision(self.wall)

    def reset(self):
        '''
        Description: Sets Paddle's score to zero.
        '''
        self._paddle_score = 0

    def draw(self):
        '''
        Description: Draws Paddle's score on the screen.
        '''
        pr.draw_text(str(self._paddle_score), self._position.x_pos, self._position.y_pos, self._font_size, self._color)

    def get_score_amount(self):
        '''
        Description: Returns the paddle score.
        '''
        return self._paddle_score

    def get_paddle_monitored(self):
        '''
        Description: Returns the paddle that the Score instance is monitoring.
        '''
        return self._monitor_side