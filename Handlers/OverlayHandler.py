from typing import Any

class OverlayHandler:
    '''
    Description: Manages and displays everything an overlay needs. (background, text, buttons)
    '''
    def __init__(self) -> None:
        self._background_list = list()
        self._text_list = list()
        self._button_list = list()

    def add(self, instance: Any, overlay_type: str):
        '''
        Description: Adds an instance object for Overlay to handle.

        Args:
        - instance (Overlay Type): An Overlay instance (BackgroundOverlay, TextOverlay, ButtonOverlay)
        - overlay_type (str): The type of overlay the instance is ("BackgroundOverlay", "TextOverlay", "ButtonOverlay")
        '''
        if overlay_type == "BackgroundOverlay":
            self._background_list.append(instance)

        elif overlay_type == "TextOverlay":
            self._text_list.append(instance)

        elif overlay_type == "ButtonOverlay":
            self._button_list.append(instance)
        
        else:
            raise TypeError

    def remove(self, instance: Any, overlay_type: str):
        '''
        Description: Removed an instance object from Overlay object.

        Args:
        - instance (Overlay Type): An Overlay instance (BackgroundOverlay, TextOverlay, ButtonOverlay)
        - overlay_type (str): The type of overlay the instance is ("BackgroundOverlay", "TextOverlay", "ButtonOverlay")
        '''
        if overlay_type == "BackgroundOverlay":
            self._background_list.remove(instance)

        elif overlay_type == "TextOverlay":
            self._text_list.remove(instance)

        elif overlay_type == "ButtonOverlay":
            self._button_list.remove(instance)
        
        else:
            raise TypeError

    def draw(self):
        '''
        Description: Draws Overlay instance.
        '''
        self.draw_background()
        self.draw_text()
        self.draw_button()

    def draw_background(self):
        '''
        Description: Draws Overlay instance's background.
        '''
        for background in self._background_list:
            background.draw()
        
    def draw_text(self):
        '''
        Description: Draws Overlay instance's text.
        '''
        for text in self._text_list:
            text.draw()
    
    def draw_button(self):
        '''
        Description: Draws Overlay's instance's buttons.
        '''
        for button in self._button_list:
            button.draw()

    def button_check(self):
        for button in self._button_list:
            button.input_check()

    def get_instances(self, overlay_type: str):
        '''
        Description: Gets all instances that match the Overlay type.

        Args:
        - overlay_type (str): The type of overlay the instance is ("BackgroundOverlay", "TextOverlay", "ButtonOverlay")
        '''
        if overlay_type == "BackgroundOverlay":
            return self._background_list

        elif overlay_type == "TextOverlay":
            return self._text_list

        elif overlay_type == "ButtonOverlay":
            return self._button_list
        
        else:
            raise TypeError

    def clear(self):
        self._background_list = list()
        self._text_list = list()
        self._button_list = list()