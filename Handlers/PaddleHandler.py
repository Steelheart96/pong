from Handlers.Handler import Handler

class PaddleHandler(Handler):
    '''
    Description: Class that manages pong paddles.
    '''
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        '''
        Description: Updates all Paddles position.

        Args:
        y_pos (int): y position update  
        '''
        for instance in self._objects:
            y_pos = instance.get_y_position()
            instance.update_position(y_pos)
    
    def reset(self):
        '''
        Description: Resets all paddle instance positions and values.
        '''
        for instance in self._objects:
            instance.reset()