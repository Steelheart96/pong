from typing import Any
from Handlers.Handler import Handler

class WallHander(Handler):
    '''
    Description: Class that manages all wall instances.
    '''
    def __init__(self,) -> None:
        super().__init__()
        self._object_types = list()

    def add(self, instance_object: Any, wall_type: str):
        '''
        Description: Adds Wall instance to Wall Handler.

        Args:
        - instance_object (Actor Subclass): An Actor subclass instance
        - wall_type (str): The type of wall it is ("visible", "invisible")
        '''
        self._objects.append(instance_object)
        self._object_types.append(wall_type)

    def remove(self, instance_object: Any):
        '''
        Description: Removes an Actor Object from the handler.

        Args:
        - instance_object (Actor Subclass): An Actor subclass instance
        '''
        instance_index = self._objects.index(instance_object)
        self._objects.remove(instance_index)
        self._object_types.remove(instance_index)

    def get_instances(self, wall_type: str):
        '''
        Description: Returns wall instance of a specific wall type.

        Args:
        - wall_type (str): The wall type to search for in Wall Handler instances ("visible", "invisible")
        '''
        object_list = []
        for instance in self._objects:
            instance_index = self._objects.index(instance)
            
            if self._object_types[instance_index] == wall_type:
                object_list.append(instance)
        return object_list

    def draw(self):
        '''
        Description: Draws all visible wall instances.
        '''
        for instance in self._objects:
            instance_index = self._objects.index(instance)
            
            if self._object_types[instance_index] == 'visible':
                instance.draw()