import pygame
from OpenGL.GL import *


class Texture:
    def __init__(self, img):
        self.texture_id = glGenTextures(1) #generate unique id for the texture
        img_load = pygame.image.load(img) # load the image file specified 
        # converts the loaded image to a raw string format that can be used as texture data.
        self.raw_img = pygame.image.tostring(img_load, "RGBA", 1) 
        self.width = img_load.get_width()
        self.height = img_load.get_height()

    def bindTexture(self):#prepare the texture by binding the texture.
        glBindTexture(GL_TEXTURE_2D, self.texture_id) #binds the texture as a 2D texture.
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        #uploads the image data to active texture, with specified width, height, format (RGBA), and data type (unsigned byte).
        glTexImage2D(GL_TEXTURE_2D, 0, 4, self.width, self.height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, self.raw_img)

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(1.0, 1.0, 1.0, 0.5)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

def texture_coord_map( s, t, x, y):
    glTexCoord2f(s, t)
    glVertex2f(x, y)
