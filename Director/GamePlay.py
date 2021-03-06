from typing import Any
from Handlers import BallHandler, ScoreHandler, WallHandler, PaddleHandler, OverlayHandler
from Overlays.BackgroundOverlay import BackgroundOverlay
from Overlays.ButtonOverlay import ButtonOverlay
from Overlays.TextOverlay import TextOverlay
from Structs import Dimensions, Window, Point
from Movement.Input import Input
from StaticObjects.Wall import Wall
from Actors.ball.Ball import Ball
from Actors.paddle.Player import Player
from Actors.paddle.Npc import npc
import pyray as pr

from Actors.paddle.ScoreText import Score


class GamePlay:
    '''
    Description: Everything that goes into creating, managing, and running the gameplay loop.

    Args:
    - window (Window): The window attributes
    - player_keys (dict): The keys the player uses to move
    - director (Director): The Dorector instance that is running the current program.
    '''
    def __init__(self, window: Window, player_keys: dict, director: Any) -> None:
        self.window = window
        self.player_keys = player_keys
        self.director = director
        self.set_up_gameplay_objects()
        self.setup_menu_overlay()

    def setup_menu_overlay(self):
        '''
        Description: Creates overlay user interacts with.
        '''
        self.setup_background_overlay()
        self.setup_title_overlay()
        self.setup_button_overlay()

        # Overlay Instance setup
        self.overlay_handler = OverlayHandler()
        self.overlay_handler.add(self.background_overlay, "BackgroundOverlay")
        self.overlay_handler.add(self.title1_overlay, "TextOverlay")
        self.overlay_handler.add(self.title2_overlay, "TextOverlay")
        self.overlay_handler.add(self.menubutton_overlay, "ButtonOverlay")
    
    def setup_background_overlay(self):
        '''
        Description: Sets up the background overlay.
        '''
        overlay_width = self.window.width // 2
        overlay_height = self.window.height
        overlay_background_color = pr.BLACK

        self.background_overlay = BackgroundOverlay(
                dimensions = Dimensions(overlay_width, overlay_height),
                color = overlay_background_color,
                screen_side = 'right',
                window_width = self.window.width
            )

    def setup_title_overlay(self):
        '''
        Description: Sets up the text Title overlay.
        '''
        overlay_title_font_size = 75
        overlay_title_color = pr.RED

        # Title Part 1
        overlay_title1_position = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8
            )
        self.title1_overlay = TextOverlay(
                text = 'Game',
                font_size = overlay_title_font_size,
                color = overlay_title_color,
                position = overlay_title1_position
            )
        
        # Title Part 2 
        overlay_title2_position = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8 * 2
            )
        self.title2_overlay = TextOverlay(
                text = 'Over',
                font_size = overlay_title_font_size,
                color = overlay_title_color,
                position = overlay_title2_position
            )

    def setup_button_overlay(self):
        '''
        Description: Sets up all button overlays.
        '''
        overlay_text_color = pr.RED
        overlay_button_dimensions = Dimensions(
                width = 100,
                height = 50
            )
        overlay_button_background_color = pr.WHITE
        
        # Menu Button Overlay
        overlay_text_menubutton = 'Menu'
        overlay_button_position_menubutton = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8 * 3
            )
        self.menubutton_overlay = ButtonOverlay(
                text = overlay_text_menubutton,
                text_color = overlay_text_color,
                position = overlay_button_position_menubutton,
                dimensions = overlay_button_dimensions,
                background_color = overlay_button_background_color,
                func_on_click = lambda: self.overlay_menubutton_func()
            )

    def overlay_menubutton_func(self):
        '''
        Description: The function the creditsbutton instance runs on click.
        '''
        self.director.playing_menu = True
        self.director.playing_game = False

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
        self.wall_handler = WallHandler()
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
        self.ball_handler.update()

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
        Description: Draws all visible objects on the screen for the gameplay loop.
        '''
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        self.score_handler.draw()

        self.paddle_handler.draw()

        self.ball_handler.draw()

        self.wall_handler.draw()

        pr.end_drawing()

    def reset(self):
        self.ball_handler.reset()
        self.paddle_handler.reset()
        self.score_handler.reset()

    def overlay_loop_draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        self.score_handler.draw()
        self.paddle_handler.draw()

        self.overlay_handler.draw()
        self.wall_handler.draw()

        pr.end_drawing()

    def overlay_loop(self):
        while self.director.playing_game and not pr.window_should_close():
            self.overlay_loop_draw()
            self.overlay_handler.button_check()

            if pr.window_should_close():
                return False

        return True


    def run(self):
        '''
        Description: The game loop for the program.
        '''
        self.reset()

        self.winner = None
        run = True
        while run:
            self.gameplay_collisions()
            self.gameplay_update()
            self.gameplay_draw()

            if self.check_for_winner():
                run = False

            if pr.window_should_close():
                return False

        game_continue = self.overlay_loop()
        
        if game_continue:
            return True
        else:
            return False