from Handlers import BallHandler, ScoreHandler, WallHander, PaddleHandler
from Structs import Dimensions, Window
from Movement.Input import Input
from StaticObjects.Wall import Wall
from Actors.ball.Ball import Ball
from Actors.paddle.Player import Player
from Actors.paddle.Npc import npc
import pyray as pr

from Text.Score import Score


class GamePlay:
    '''
    Description: Everything that goes into creating, managing, and running the gameplay loop.
    '''
    def __init__(self, window: Window, player_keys: dict) -> None:
        self.window = window
        self.player_keys = player_keys
        self.set_up_gameplay_objects()

    def set_up_gameplay_objects(self):
        '''
        Description: Creates objects used in the gameplay program loop.
        '''

        # Individual Objects
        top_bottom_wall_height = self.gameplay_wall_setup()
        self.gameplay_ball_setup()
        self.gameplay_paddle_setup(top_bottom_wall_height)
        self.gameplay_score_setup()

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

        # Score Handler
        self.score_handler = ScoreHandler()
        self.score_handler.add(self.player_score)
        self.score_handler.add(self.ai_score)

    def gameplay_wall_setup(self):
        '''
        Description: Wall object gameplay loop setup.

        Returns:
        - int: Height of top and bottom Wall instance heights
        '''
        top_bottom_wall_height = 20
        left_right_wall_width = 20

        # border walls
        self.top_wall = Wall(self.window.width, top_bottom_wall_height, 0, 0, pr.RED)
        self.bottom_wall = Wall(self.window.width, top_bottom_wall_height, 0, self.window.height - top_bottom_wall_height, pr.RED)

        # endzone walls
        self.left_wall = Wall(left_right_wall_width, self.window.height, 0, 0, pr.BLANK)
        self.right_wall = Wall(left_right_wall_width, self.window.height, self.window.width - left_right_wall_width, 0, pr.BLANK)

        return top_bottom_wall_height

    def gameplay_ball_setup(self):
        '''
        Description: Ball object gameplay loop setup.
        '''
        self.ball = Ball(self.window, 5, pr.WHITE)

    def gameplay_score_setup(self):
        '''
        Description: Score instance gameplay loop setup.
        '''
        self.player_score = Score(self.window, self.right_wall, self.ball, "left", 100, pr.BLUE)
        self.ai_score = Score(self.window, self.left_wall, self.ball, "right", 100, pr.BLUE)

    def gameplay_paddle_setup(self, top_bottom_wall_height: int):
        '''
        Description: Paddle objects and Input gameplay loop setup.

        Args:
        - top_bottom_wall_height (int): The height of the top and bottom Wall instance
        '''
        # Input Monitor Creation
        self.player_input = Input(self.player_keys, top_bottom_wall_height, self.window.height)

        # Paddle Creation
        paddle_color = pr.WHITE
        paddle_dimensions = Dimensions(10, 40)
        self.player = Player(self.window, paddle_dimensions, paddle_color, 'left', self.player_input)
        self.ai_paddle = npc(self.window, paddle_dimensions, paddle_color, 'right', self.ball, top_bottom_wall_height)
    
    def gameplay_update(self):
        '''
        Description: Computes all object actions.
        '''
        self.ball.update_position()

        self.paddle_handler.update()
    
    def gameplay_collisions(self):
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
        self.score_handler.update()
        self.ball_handler.reset()
        self.paddle_handler.reset()
        self.player_input.reset_velocity()
        self.winner = self.score_handler.check_for_win()

    def check_for_winner(self):
        if self.winner != None:
            return True
        else:
            return False

    def gameplay_draw(self):
        '''
        Description: Draws all visible objects on the screen.
        '''
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        self.score_handler.draw()

        self.paddle_handler.draw()

        self.ball_handler.draw()

        self.wall_handler.draw()

        pr.end_drawing()

    def run(self):
        '''
        Description: The game loop for the program.
        '''
        self.winner = None
        run = True
        while not pr.window_should_close() and run:
            self.gameplay_collisions()
            self.gameplay_update()
            self.gameplay_draw()

            if self.check_for_winner():
                run = False
        
        # keeps program Director loop running if there is a winner
        if run == False:
            return False
        else:
            return True