from Structs.Window import Window
from Structs.Point import Point
from wall.Wall import Wall
from Actors.ball.Ball import Ball
from Actors.paddle.Player import Player
from Actors.paddle.Npc import npc
from Actors.Load import Load
import pyray as pr

class Director:
    '''
    Description: Creates and controls all main game logic.

    Args:
    - window (Window): Information about the window
    '''

    def __init__(self, window: Window) -> None:
        self.window = window
        self.initialize_window()
        self.set_up_objects()

    def initialize_window(self):
        '''
        Description: Initializes pyray program window.
        '''
        pr.init_window(*self.window.pr_window_setup())
        pr.set_target_fps(self.window.fps_cap)

    def set_up_objects(self):
        '''
        Description: Creates objects used in the program.
        '''
        # Wall Creation
        wall_height = 20

        top_wall_position = Point(0, 0)
        bottom_wall_position = Point(0, self.window.height - wall_height)

        self.top_wall = Wall(self.window, wall_height, top_wall_position, pr.RED)
        self.bottom_wall = Wall(self.window, wall_height, bottom_wall_position, pr.RED)

        # Ball Creation
        self.ball = Ball(self.window, 5, pr.WHITE)

        # Paddle Creation
        paddle_texture = Load.image_file_to_texture('TwitterIcon.png')
        self.paddle1 = Player(self.window, paddle_texture, 'left')
        self.paddle2 = npc(self.window, paddle_texture, 'right', self.ball)

    def run(self):
        '''
        Description: The game loop for the program.
        '''
        while not pr.window_should_close():
            self.update()
            self.draw()
            self.collision()

    def update(self):
        '''
        Description: Computes all objects actions.
        '''
        self.ball.update_position(1, 0)
        self.ball_colide_p_2 = self.ball.check_collision(self.paddle2)
        self.ball_colide_p_1 = self.ball.check_collision(self.paddle1)

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
    
    def collision(self):
        '''
        Description: Response to collisions.
        '''
        if self.ball_colide_p_2:
            print('hit paddle 2!')
        if self.ball_colide_p_1:
            print('hit paddle 1!')
        
    def close(self):
        '''
        Description: Closes pyray program window.
        '''
        pr.close_window()