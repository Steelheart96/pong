from Handlers.Handler import Handler
from Movement.Input import Input
from StaticObjects.Wall import Wall

class BallHandler(Handler):
    '''
    Description: Class that manages Ball instances.

    Args:
    - paddles (list): List of Paddle instances
    - visible_walls (list): List of wall instances drawn on screen
    - goal_walls (list): List of wall instances not drawn on screen
    '''

    def __init__(self, paddles: list, visible_walls: list, goal_walls: list) -> None:
        super().__init__()
        self.paddles = paddles
        self.visible_walls = visible_walls
        self.goal_walls = goal_walls

    def update(self):
        '''
        Description: Updates Ball instance positions
        '''
        for ball in self._objects:
            ball.update_position()

    def visible_object_collided(self, direction: str, velocity_update: bool = True):
        '''
        Description: Checks for collisions with visible objects.

        Args:
        - Direction (str): The object the ball collided with ('paddle' | 'wall')
        - velocity_update (bool): Whether or not the ball instance velocities get updated
        '''
        for ball in self._objects:
            if direction.lower() == "paddle":
                ball.flip_x_velocity()
                if velocity_update:
                    ball.update_velocity_x()
            else:
                ball.flip_y_velocity()
                if velocity_update:
                    ball.update_velocity_y()

    def paddle_collision_check(self):
        '''
        Description: Checks for ball collisions with paddles.
        '''
        for ball in self._objects:
            for paddle in self.paddles:
                collision = ball.check_collision(paddle)

                if collision:
                    return True
        return False

    def visible_wall_collision_check(self):
        '''
        Description: Checks for ball collisions with visible walls.
        '''
        for ball in self._objects:
            for wall in self.visible_walls:
                collision = ball.check_collision(wall)

                if collision:
                    return True
        return False
    
    def goal_wall_collision_check(self):
        '''
        Description: Checks for ball collisions with invisible walls.
        '''
        for ball in self._objects:
            for wall in self.goal_walls:
                collision = ball.check_collision(wall)

                if collision:
                    return True
        return False

    def reset(self):
        for ball in self._objects:
            ball.reset()