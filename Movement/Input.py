from Actors.paddle.Player import Player
import pyray as pr

class Input:
    '''
    Description: Takes user input and updates a player instance.

    Args:
    - player_paddle (Player): A Player instance paddle
    - player_keys (dict): The keyboard inputs that the program will look for as well as the response to those inputs.
    '''

    def __init__(self, player_paddle: Player, player_keys: dict) -> None:
        self._player = player_paddle
        self._player_keys = player_keys
        self.player_movement_speed = 5

    def process(self):
        '''
        Description: Processes keyboard inputs.
        '''
        for button_key, number_value in self._player_keys.items():
            if pr.is_key_down(button_key):
                y_pos = number_value(0, self.player_movement_speed)
                self._player.update_position(y_pos)

    def reset_velocity(self):
        '''
        Description: Resets Player instance's velocity.
        '''
        self.player_movement_speed = 5
    
    def update_player_velocity(self):
        '''
        Description: Adds 1 to player velocity when called.
        '''
        self.player_movement_speed += 1