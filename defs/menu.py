import pygame
pygame.init()
from os import listdir

def load_menu(cls):
    preload = cls("default.png")
    menulist = listdir(preload.path)
    objs = []
    for entry in menulist:
        obj = cls(entry)
        objs.append(obj)
    return objs