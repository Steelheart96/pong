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