import pyray as pr

class Input:
    '''
    Description: Takes user input and updates a player instance.

    Args:
    - player_keys (dict): The keyboard inputs that the program will look for as well as the response to those inputs.
    - top_bottom_wall_height (int): The top and bottom window Wall height
    - window_height (int): The height of the program window
    '''

    Default_player_speed = 5
    Max_player_speed = 20
    Player_speed_update_amount = 1

    def __init__(self, player_keys: dict, top_bottom_wall_height: int, window_height: int) -> None:
        self._player_keys = player_keys
        self.top_bottom_wall_height = top_bottom_wall_height
        self.window_height = window_height
        self.player_movement_speed = Input.Default_player_speed

    def process(self, player_y_pos: int, player_height: int):
        '''
        Description: Processes keyboard inputs and keeps player inside wall borders.

        Args:
        - player_y_pos (int): y position of the player
        - player_height (int): height of the player
        '''
        y_pos = 0
        for button_key, number_value in self._player_keys.items():
            if pr.is_key_down(button_key):
                y_pos += number_value(0, self.player_movement_speed)

        if self.top_bottom_wall_height < player_y_pos + y_pos < self.window_height - self.top_bottom_wall_height - player_height:
            return y_pos
        else:
            return int(0)

    def reset_velocity(self):
        '''
        Description: Resets Player instance's velocity.
        '''
        self.player_movement_speed = Input.Default_player_speed
    
    def update_player_velocity(self):
        '''
        Description: Adds an amount to player velocity when called.
        '''
        if self.player_movement_speed < Input.Max_player_speed:
            self.player_movement_speed += Input.Player_speed_update_amount