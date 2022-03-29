from Actors.Actor import Actor
from Structs import Point, Window
import pyray as pr
from random import choice, randint

class Ball(Actor):
    '''
    Description: The class for creating and managing ball Actors.
    
    Args:
    - window (Window): The programs information about the Window
    - radius (int): The radius of the ball
    - color (pr.Color): The color of the ball
    '''

    x_velocity_update_amount = 1
    y_velocity_update_amount = 1

    def __init__(self, window: Window, radius: int, color: pr.Color):
        super().__init__(window)
        self._radius = radius
        self.color = color
        self.set_start_position()
        self.randomize_velocity()

    def update_position(self):
        '''
        Description: Ball update coordinates function.

        Args:
        - x_pos (int): x position update
        - y_pos (int): y position update
        '''
        self._position.x_pos += self._velocity_x
        self._position.y_pos += self._velocity_y

    def set_start_position(self):
        '''
        Description: Sets the start position of the ball.
        '''
        self._position = Point(self.window.width // 2, self.window.height // 2)

    def randomize_velocity(self):
        '''
        Description: Sets the velocity for the Ball instance at the start of the game.
        '''
        self._velocity_x = choice([3, -3])
        self._velocity_y = 0
        while self._velocity_y == 0:
            self._velocity_y = randint(-3, 3)

    def draw(self):
        '''
        Description: Draws the ball onto the screen.
        '''
        pr.draw_circle(self._position.x_pos, self._position.y_pos, self._radius, self.color)

    def check_collision(self, paddle):
        '''
        Description: Checks for a collision with the player or the npc.

        Args:
        - paddle (npc or Player): Either the Player instance or npc instance

        Returns:
        - bool: True - Ball has collided | False - Ball has not collided
        '''
        return pr.check_collision_circle_rec(
            pr.Vector2(self._position.x_pos, self._position.y_pos),
            self._radius,
            pr.Rectangle(paddle.get_position().x_pos, paddle.get_position().y_pos, paddle.get_width(), paddle.get_height())
        )
    
    def get_pos_y(self):
        '''
        Description: Gets Ball instances y position.
        '''
        return self._position.y_pos

    def get_radius(self):
        '''
        Description: Gets Bal instances radius.
        '''
        return self._radius

    def flip_x_velocity(self):
        '''
        Description: Flips the Ball instance's direction on the x axis.
        '''
        self._velocity_x *= -1
        Ball.x_velocity_update_amount * -1

    def flip_y_velocity(self):
        '''
        Description: Flips the Ball instance's direction on the y axis.
        '''
        self._velocity_y *= -1
        Ball.y_velocity_update_amount * -1

    def check_velocity(velocity: int):
        '''
        Description: Checks to see if velocity is positive or negative.

        Returns:
        - bool: positive int is True | negative int is False
        '''
        if velocity > 0:
            return True
        else:
            return False

    def reset_velocity(self):
        '''
        Description: Resets Ball velocity to 1.
        '''
        Ball.velocity_update_amount = 1

    def update_velocity_x(self):
        '''
        Description: Adds 1 to x velocity when x velocity is positive.
        '''
        if Ball.check_velocity(self._velocity_x):
            self._velocity_x += Ball.x_velocity_update_amount

    def update_velocity_y(self):
        '''
        Description: Adds 1 to y velocity when y velocity is positive.
        '''
        if Ball.check_velocity(self._velocity_y):
            self._velocity_y += Ball.y_velocity_update_amount

    def reset(self):
        '''
        Description: Resets Ball instance position and velocity. Resets Ball velocity.
        '''
        self.set_start_position()
        self.randomize_velocity()
        self.reset_velocity()