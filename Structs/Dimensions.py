from dataclasses import dataclass

@dataclass
class Dimensions:
    '''
    Struct

    Args:
    - width (int): width dimension
    - height (int): height dimension
    '''
    width: int
    height: int

    def copy(self):
        '''
        Description: Returns a COPY of a Dimensions instance.
        '''
        return Dimensions(self.width, self.height)