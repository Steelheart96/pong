from typing import Any
from Actors.ball.Ball import Ball
from Actors.paddle.Npc import npc
from Handlers import BallHandler, OverlayHandler, PaddleHandler, WallHandler
from Overlays.BackgroundOverlay import BackgroundOverlay
from Overlays.TextOverlay import TextOverlay
from Overlays.ButtonOverlay import ButtonOverlay
from StaticObjects.Wall import Wall
from Structs import Dimensions, Window, Point
import pyray as pr


class Menu:
    '''
    Description: Everything that goes into creating, managing, and running the gameplay loop.

    Args:
    - window (Window): The window attributes
    - director (Director): The Dorector instance that is running the current program.
    '''
    def __init__(self, window: Window, director: Any) -> None:
        self.window = window
        self.director = director
        self.setup_menu_background()
        self.setup_menu_overlay()

    def setup_menu_overlay(self):
        '''
        Description: Creates overlay user interacts with.
        '''
        self.setup_background_overlay()
        self.setup_text_overlay()
        self.setup_button_overlay()

        # Overlay Instance setup
        self.overlay_handler = OverlayHandler()
        self.overlay_handler.add(self.background_overlay, "BackgroundOverlay")
        self.overlay_handler.add(self.title1_overlay, "TextOverlay")
        self.overlay_handler.add(self.title2_overlay, "TextOverlay")
        self.overlay_handler.add(self.playbutton_overlay, "ButtonOverlay")
        self.overlay_handler.add(self.creditsbutton_overlay, "ButtonOverlay")
        self.overlay_handler.add(self.quitbutton_overlay, "ButtonOverlay")
    
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

    def setup_text_overlay(self):
        '''
        Description: Sets up the text overlay.
        '''
        overlay_title_font_size = 50
        overlay_title_color = pr.RED

        # Title Part 1
        overlay_title1_position = Point(
                x_pos = self.window.width // 10 * 7,
                y_pos = self.window.height // 8
            )
        self.title1_overlay = TextOverlay(
                text = 'Impossible',
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
                text = 'Pong',
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
        
        # Play Button Overlay
        overlay_text_playbutton = 'Play'
        overlay_button_position_playbutton = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8 * 4
            )
        self.playbutton_overlay = ButtonOverlay(
                text = overlay_text_playbutton,
                text_color = overlay_text_color,
                position = overlay_button_position_playbutton,
                dimensions = overlay_button_dimensions,
                background_color = overlay_button_background_color,
                func_on_click = lambda: self.overlay_playbutton_func(self.director)
            )
        
        # Credits Button Overlay
        overlay_text_creditsbutton = 'Credits'
        overlay_button_position_creditsbutton = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8 * 5
            )
        self.creditsbutton_overlay = ButtonOverlay(
                text = overlay_text_creditsbutton,
                text_color = overlay_text_color,
                position = overlay_button_position_creditsbutton,
                dimensions = overlay_button_dimensions,
                background_color = overlay_button_background_color,
                func_on_click = lambda: self.overlay_creditsbutton_func(self.director)
            )
        
        # Quit Button Overlay
        overlay_text_quitbutton = 'Quit'
        overlay_button_position_quitbutton = Point(
                x_pos = self.window.width // 4 * 3,
                y_pos = self.window.height // 8 * 6
            )
        self.quitbutton_overlay = ButtonOverlay(
                text = overlay_text_quitbutton,
                text_color = overlay_text_color,
                position = overlay_button_position_quitbutton,
                dimensions = overlay_button_dimensions,
                background_color = overlay_button_background_color,
                func_on_click = lambda: self.overlay_quitbutton_func()
            )

    def overlay_playbutton_func(self, director: Any):
        '''
        Description: The function the playbutton instance runs on click.

        Args:
        - director (Director): The director instance running the program 
        '''
        director.playing_game = True
        director.playing_menu = False
        self.run_loop = False

    def overlay_creditsbutton_func(self, director: Any):
        '''
        Description: The function the creditsbutton instance runs on click.

        Args:
        - director (Director): The director instance running the program 
        '''
        director.playing_credits = True
        director.playing_menu = False
        self.run_loop = False

    def overlay_quitbutton_func(self):
        '''
        Description: The function the quitbutton instance runs on click.
        '''
        self.run_loop = False

    def setup_menu_background(self):
        '''
        Description: Creates objects used in the menu background program loop.
        '''
        # Individual Objects
        top_bottom_wall_height = self.menu_wall_setup()
        self.menu_ball_setup()
        self.menu_paddle_setup(top_bottom_wall_height)

        # Handler Setup
        self.paddle_handler = PaddleHandler()
        self.paddle_handler.add(self.ai_paddle_right)
        self.paddle_handler.add(self.ai_paddle_left)

        self.wall_handler = WallHandler()
        self.wall_handler.add(self.top_wall, "visible")
        self.wall_handler.add(self.bottom_wall, "visible")

        self.ball_handler = BallHandler(
                self.paddle_handler.get_instances(),
                self.wall_handler.get_instances('visible'),
                list()
            )
        self.ball_handler.add(self.ball)

    def menu_wall_setup(self):
        '''
        Description: Wall object menu loop setup.

        Returns:
        - int: Height of top and bottom Wall instance heights and right Wall instance width
        '''
        top_bottom_wall_height = 20

        # border walls
        self.top_wall = Wall(self.window.width, top_bottom_wall_height, 0, 0, pr.RED)
        self.bottom_wall = Wall(self.window.width, top_bottom_wall_height, 0, self.window.height - top_bottom_wall_height, pr.RED)

        return top_bottom_wall_height

    def menu_ball_setup(self):
        '''
        Description: Ball object gameplay loop setup.
        '''
        self.ball = Ball(self.window, 5, pr.WHITE, menu_displaying = True)
    
    def menu_paddle_setup(self, top_bottom_wall_height: int):
        '''
        Description: Paddle objects and Input menu loop setup.

        Args:
        - top_bottom_wall_height (int): The height of the top and bottom Wall instance
        '''
        paddle_color = pr.WHITE
        paddle_dimensions = Dimensions(10, 40)
        self.ai_paddle_left = npc(
                self.window,
                paddle_dimensions,
                paddle_color,
                'left',
                self.ball,
                top_bottom_wall_height
            )
        self.ai_paddle_right = npc(
                self.window,
                paddle_dimensions,
                paddle_color,
                'right',
                self.ball,
                top_bottom_wall_height
            )

    def menu_update(self):
        '''
        Description: Computes all object actions.
        '''
        self.ball_handler.update()

        self.paddle_handler.update()
    
    def menu_logic(self):
        '''
        Description: Response to collisions.
        '''
        if self.ball_handler.paddle_collision_check():
            self.ball_handler.visible_object_collided('paddle', velocity_update = False)

        if self.ball_handler.visible_wall_collision_check():
            self.ball_handler.visible_object_collided('visible wall', velocity_update = False)
        
        self.overlay_handler.button_check()

    def menu_draw(self):
        '''
        Description: Draws all visible objects on the screen for the menu loop.
        '''
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        self.paddle_handler.draw()
        self.ball_handler.draw()
        self.overlay_handler.draw()
        self.wall_handler.draw()

        pr.end_drawing()
    
    def run(self):
        '''
        Description: The menu loop for the program.
        '''
        
        self.run_loop = True
        while self.run_loop:
            self.menu_logic()
            self.menu_update()
            self.menu_draw()

            if pr.window_should_close():
                return False

        return False