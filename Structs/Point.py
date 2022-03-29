from dataclasses import dataclass

@dataclass
class Point:
    '''
    Dataclass

    Args:
    - x_pos (int): x position
    - y_pos (int): y position
    '''
    x_pos: int
    y_pos: int

    def copy(self):
        '''
        Description: Returns a COPY of a Point instance.
        '''
        return Point(self.x_pos, self.y_pos)