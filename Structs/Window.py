from dataclasses import dataclass

@dataclass
class Window:
    '''
    Dataclass

    Args:
    - width (int): Width of the window
    - height (int): height of the window
    - caption (str): caption of the window
    - fps_cap (int): fps of the window
    '''
    width: int
    height: int
    caption: str
    fps_cap: int

    def copy(self):
        '''
        Description: Returns a COPY of a Window instance.
        '''
        return Window(self.width, self.height, self.caption, self.fps_cap)