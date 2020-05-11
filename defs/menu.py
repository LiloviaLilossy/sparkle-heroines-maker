import pygame
pygame.init()
from os import listdir

class Menu:
    def __init__(self, cls):
        self.cls=cls
    
    def load_menu():
        preload = self.cls("default.png")
        menulist = listdir(preload.path)
        objs = []
        for entry in menulist:
            obj = self.cls(entry)
            objs.append(obj)
        return objs
    
    def change_menu(cls):
        self.cls=cls
        load_menu()