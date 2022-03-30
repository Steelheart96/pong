from typing import Any

class Handler:
    '''
    Description: Base Handler class.
    '''

    def __init__(self) -> None:
        self._objects = list()

    def add(self, instance_object: Any):
        '''
        Description: Adds an Actor Object to the handler.

        Args:
        - instance_object (Actor Subclass): An Actor subclass instance
        '''
        self._objects.append(instance_object)

    def remove(self, instance_object: Any):
        '''
        Description: Removes an Actor Object from the handler.

        Args:
        - instance_object (Actor Subclass): An Actor subclass instance
        '''
        self._objects.remove(instance_object)

    def get_instances(self):
        '''
        Description: Returns a list of instances in Handler list.

        Returns:
        - list: List of instances in objects list
        '''
        return self._objects

    def clear(self):
        '''
        Description: Clears all object instances from Handler list.
        '''
        self._objects.clear()

    def draw(self):
        '''
        Description: Draw function for instance objects in Handler.
        '''
        for instance in self._objects:
            instance.draw()