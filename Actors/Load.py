import pyray as pr

class Load:
    '''
    Description: A class that holds methods for creating images, loading textures, and drawing rectangles.
    '''

    def text_to_image(character:str , font_size:int , color: pr.Vector4) -> pr.Image:
        '''
        Description: Creates an image from text
        
        Returns:
        - pr.Image
        '''
        return pr.image_text(character, font_size, color)

    def image_file_to_image(image: str):
        '''
        Description: Takes an image file and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        return pr.load_image(image)

    def image_file_to_texture(image: str):
        '''
        Description: Takes an image file and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        image = pr.load_image(image)
        return pr.load_texture_from_image(image)
    
    def image_to_texture(image: pr.Image):
        '''
        Description: Takes an image and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        return pr.load_texture_from_image(image)

    def text_to_texture(character: str, font_size: int, color: pr.Color) -> pr.Texture:
        '''
        Description: Takes a string and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        image = pr.image_text(character, font_size, color)
        return pr.load_texture_from_image(image)
    
    def draw_rectangle(actor) -> None:
        '''
        Description: Creates a rectangle, renders it's texture, and places it on screen

        Args:
        - actor (Actor): An instance of a Player or Tail
        '''
        pr.draw_texture_rec(
            actor.texture,
            pr.Rectangle(0,0, float(actor.texture.width), float(actor.texture.height)),
            [actor.pos_x, actor.pos_y],
            pr.WHITE
        )