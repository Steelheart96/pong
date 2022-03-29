from Structs import Window

class Actor:
    '''
    Description: Base class for all Actors.

    Args:
    - window (Window): The programs information about the Window
    '''
    
    def __init__(self, window: Window):
        self.window = window

    def update_position(self):
        '''
        Description: Default behavior for updating x/y coordinates.
        '''
        raise NotImplementedError

    def set_start_position(self):
        '''
        Description: Default behavior for setting actor's default position.
        '''
        raise NotImplementedError

    def draw(self):
        '''
        Description: Default behavior for drawing an actor. 
        '''
        raise NotImplementedError