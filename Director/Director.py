from Movement.Input import Input
from Structs import Dimensions, Window
from Border.Wall import Wall
from Actors.ball.Ball import Ball
from Actors.paddle.Player import Player
from Actors.paddle.Npc import npc
import pyray as pr

class Director:
    '''
    Description: Creates and controls all main game logic.

    Args:
    - window (Window): Information about the window
    - player_keys (dict): The player keys to look for input from ("input type": "outcome")
    '''

    def __init__(self, window: Window, player_keys: dict) -> None:
        self.window = window
        self.player_keys = player_keys
        self.initialize_window()
        self.set_up_objects()

    def initialize_window(self):
        '''
        Description: Initializes pyray program window.
        '''
        pr.init_window(self.window.width, self.window.height, self.window.caption)
        pr.set_target_fps(self.window.fps_cap)

    def set_up_objects(self):
        '''
        Description: Creates objects used in the program.
        '''
        # Wall Creation
        top_bottom_wall_height = 20
        left_right_wall_width = 20

        self.top_wall = Wall(self.window.width, top_bottom_wall_height, 0, 0, pr.RED)
        self.bottom_wall = Wall(self.window.width, top_bottom_wall_height, 0, self.window.height - top_bottom_wall_height, pr.RED)

        self.left_wall = Wall(left_right_wall_width, self.window.height, 0, 0, pr.BLANK)
        self.right_wall = Wall(left_right_wall_width, self.window.height, self.window.width - left_right_wall_width, 0, pr.BLANK)

        # Ball Creation
        self.ball = Ball(self.window, 5, pr.WHITE)

        # get top and bottom wall height for NPC
        self.top_wall_height = self.top_wall.get_height()
        self.bottom_wall_height = self.bottom_wall.get_height()

        # Paddle Creation
        paddle_color = pr.WHITE
        paddle_dimensions = Dimensions(20, 40)
        self.paddle1 = Player(self.window, paddle_dimensions, paddle_color, 'left')
        self.paddle2 = npc(self.window, paddle_dimensions, paddle_color, 'right', self.ball, self.top_wall_height, self.bottom_wall_height)

        # Input Monitor Creation
        self.player_input = Input(self.paddle1, self.player_keys)

    def run(self):
        '''
        Description: The game loop for the program.
        '''
        while not pr.window_should_close():
            self.player_input.process()
            self.update()
            self.collision_response()
            self.draw()

    def update(self):
        '''
        Description: Computes all object actions.
        '''
        self.ball.update_position()
        self.paddle2.set_location()

        self.ball_colide_p_2 = self.ball.check_collision(self.paddle2)
        self.ball_colide_p_1 = self.ball.check_collision(self.paddle1)

        self.ball_colide_top_wall = self.ball.check_collision(self.top_wall)
        self.ball_colide_bottom_wall = self.ball.check_collision(self.bottom_wall)

        self.ball_collide_left_wall = self.ball.check_collision(self.left_wall)
        self.ball_collide_right_wall = self.ball.check_collision(self.right_wall)
    
    def collision_response(self):
        '''
        Description: Response to collisions.
        '''
        if self.ball_colide_p_2 or self.ball_colide_p_1:
            self.visible_object_colide_response("x")
        if self.ball_colide_top_wall or self.ball_colide_bottom_wall:
            self.visible_object_colide_response("y")
        if self.ball_collide_left_wall or self.ball_collide_right_wall:
            self.goal_collide_response()
    
    def visible_object_colide_response(self, direction: str):
        '''
        Description: Response to ball colliding with visible objects.
        '''
        if direction == "x":
            self.ball.flip_x_velocity()
            self.ball.update_velocity_x()
        else:
            self.ball.flip_y_velocity()
            self.ball.update_velocity_y()

        self.player_input.update_player_velocity()
    
    def goal_collide_response(self):
        '''
        Description: Response to ball colliding with the goal zones.
        '''
        self.ball.reset()
        self.paddle1.reset()
        self.paddle2.reset()
        self.player_input.reset_velocity()

    def draw(self):
        '''
        Description: Draws all visible objects on the screen.
        '''
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        self.paddle1.draw()
        self.paddle2.draw()

        self.ball.draw()

        self.top_wall.draw()
        self.bottom_wall.draw()
        pr.end_drawing()
        
    def close(self):
        '''
        Description: Closes pyray program window.
        '''
        pr.close_window()