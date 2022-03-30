from Handlers.Handler import Handler

class ScoreHandler(Handler):
    '''
    Description: Class that manages all Score instances.
    '''

    Score_Win_Amount = 5

    def __init__(self) -> None:
        super().__init__()

    def update(self):
        '''
        Description: Updates the Score instances.
        '''
        for instance in self._objects:
            instance.update()

    def check_for_win(self):
        for instance in self._objects:
            if instance.get_score_amount() >= ScoreHandler.Score_Win_Amount:
                return instance.get_paddle_monitored()
        return None

    def reset(self):
        '''
        Description: Resets the Score instances.
        '''
        for instance in self._objects:
            instance.reset()