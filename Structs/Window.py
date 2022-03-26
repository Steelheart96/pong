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

    
    def pr_window_setup(self):
        return self.width, self.height, self.fps_cap, self.caption