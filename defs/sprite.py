from pygame.sprite import Sprite
import pygame
pygame.init()

class Base(Sprite):
    def __init__(self):

        # Init
        super().__init__()

        # Central position
        self.x=250
        self.y=360

        # Image
        self.base_image=pygame.image.load("sprites/body.png").convert_alpha()
        self.rect=self.base_image.get_rect(center=(self.x,self.y))
        self.base_eyes=pygame.image.load("sprites/eyes.png").convert_alpha()
        self.eyes_rect=self.base_eyes.get_rect(center=(self.x,self.y))

        # Variables
        self.name="base body"
        self.base_color="#FFEDCC"
        self.base_age=13
        self.base_eyecolor="#00FF00"
        self.base_smile="happy"
        self.base_eyebrows="standard"

class Hair(Sprite):
    def __init__(self, hair):
        
        # Init
        super().__init__()
        self.path="sprites/hair/"

        # Central position
        self.x=100
        self.y=100

        # Image
        self.base_image=pygame.image.load(self.path+hair).convert_alpha()
        self.rect=self.base_image.get_rect(center=(self.x,self.y))

        # Variables
        self.base_color="#66000"