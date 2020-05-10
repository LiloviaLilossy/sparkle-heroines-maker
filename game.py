import pygame
from defs.sprite import *
from defs.menu import load_menu
pygame.init()

sc = pygame.display.set_mode((1280,720))

body = Base()
menu = load_menu(Hair)

MENU_ENTRY_START_X = 780
MENU_ENTRY_START_Y = 50

game=True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
    sc.fill((255,255,255))
    sc.blit(body.base_image, body.rect)
    sc.blit(body.base_eyes, body.eyes_rect)
    for i in range(len(menu)):
        menu[i].rect.x = MENU_ENTRY_START_X+150*(i+1)
        #menu[i].rect.y = MENU_ENTRY_START_Y+20*(i+1)
        menu[i].rect.y = MENU_ENTRY_START_Y
        sc.blit(menu[i].base_image, menu[i].rect)
    pygame.display.update()