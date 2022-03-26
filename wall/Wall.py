import pyray as pr
from Structs.Point import Point
from Structs.Window import Window

class Wall:
    '''
    Description: A class for creating and managing walls.
    '''

    def __init__(self, window: Window, height: int, position: Point, color: pr.Color) -> None:
        self.window = window
        self.height = height
        self.position = position
        self.color = color

    def draw(self):
        pr.draw_rectangle(self.position.x_pos, self.position.y_pos, self.window.width, self.height, self.color)