from Handlers.BallHandler import BallHandler
from Handlers.WallHandler import WallHander
from Handlers.PaddleHandler import PaddleHandler
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

        # Individual Objects
        top_bottom_wall_height, left_right_wall_width = self.wall_setup()
        self.ball_setup()
        self.paddle_setup(top_bottom_wall_height, left_right_wall_width)

        # Paddle Handler
        self.paddle_handler = PaddleHandler()
        self.paddle_handler.add(self.player)
        self.paddle_handler.add(self.ai_paddle)

        # Wall Handler
        self.wall_handler = WallHander()
        self.wall_handler.add(self.top_wall, "visible")
        self.wall_handler.add(self.bottom_wall, "visible")
        self.wall_handler.add(self.left_wall, "invisible")
        self.wall_handler.add(self.right_wall, "invisible")

        # Ball Handler
        self.ball_handler = BallHandler(
                self.paddle_handler.get_instances(),
                self.wall_handler.get_instances('visible'),
                self.wall_handler.get_instances('invisible')
                )
        self.ball_handler.add(self.ball)

    def wall_setup(self):
        '''
        Description: Wall object setup.
        '''
        top_bottom_wall_height = 20
        left_right_wall_width = 20

        # border walls
        self.top_wall = Wall(self.window.width, top_bottom_wall_height, 0, 0, pr.RED)
        self.bottom_wall = Wall(self.window.width, top_bottom_wall_height, 0, self.window.height - top_bottom_wall_height, pr.RED)

        # endzone walls
        self.left_wall = Wall(left_right_wall_width, self.window.height, 0, 0, pr.BLANK)
        self.right_wall = Wall(left_right_wall_width, self.window.height, self.window.width - left_right_wall_width, 0, pr.BLANK)

        return top_bottom_wall_height, left_right_wall_width

    def ball_setup(self):
        '''
        Description: Ball objects setup.
        '''
        self.ball = Ball(self.window, 5, pr.WHITE)

    def paddle_setup(self, top_wall_height: int, bottom_wall_height: int):
        '''
        Description: Paddle objects and Input setup.

        Args:
        - top_wall_height (int): The height of the top Wall instance
        - bottom_wall_height (int): The height of the bottom Wall instance
        '''
        # Input Monitor Creation
        self.player_input = Input(self.player_keys, top_wall_height, bottom_wall_height, self.window.height)

        # Paddle Creation
        paddle_color = pr.WHITE
        paddle_dimensions = Dimensions(10, 40)
        self.player = Player(self.window, paddle_dimensions, paddle_color, 'left', self.player_input)
        self.ai_paddle = npc(self.window, paddle_dimensions, paddle_color, 'right', self.ball, top_wall_height, bottom_wall_height)

    def run(self):
        '''
        Description: The game loop for the program.
        '''
        while not pr.window_should_close():
            self.collisions()
            self.update()
            self.draw()

    def update(self):
        '''
        Description: Computes all object actions.
        '''
        self.ball.update_position()

        self.paddle_handler.update()
    
    def collisions(self):
        '''
        Description: Response to collisions.
        '''
        if self.ball_handler.paddle_collision_check():
            self.ball_handler.visible_object_collided('paddle')
            self.player_input.update_player_velocity()

        if self.ball_handler.visible_wall_collision_check():
            self.ball_handler.visible_object_collided('visible wall')
            self.player_input.update_player_velocity()

        if self.ball_handler.goal_wall_collision_check():
            self.goal_collide_response()
    
    def goal_collide_response(self):
        '''
        Description: Response to ball colliding with the goal zones.
        '''
        self.ball_handler.reset()
        self.paddle_handler.reset()
        self.player_input.reset_velocity()

    def draw(self):
        '''
        Description: Draws all visible objects on the screen.
        '''
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        self.paddle_handler.draw()

        self.ball_handler.draw()

        self.wall_handler.draw()

        pr.end_drawing()
        
    def close(self):
        '''
        Description: Closes pyray program window.
        '''
        pr.close_window()