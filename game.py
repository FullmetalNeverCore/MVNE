import pygame
from mvne import *

pygame.init()


WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


run = True

text = MVNE_classic_text_control(screen,'Hello World!',WINDOW_SIZE)

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of the black box
                # Change the text to "Clicked!"
                prev_t = text
                transit3.fadeout()
                text = MVNE_classic_text_control(screen,'Clicked!',WINDOW_SIZE)
                text.p_obj_surf = prev_t.text
                start_time = pygame.time.get_ticks()

    x = pygame.image.load("background.png").convert()
    y = pygame.image.load("foreground.png").convert_alpha()

    bg = MVNE_classic_img(screen,x)
    fg = MVNE_classic_img(screen,y)
    transit = MVNE_classic_transitions(start_time,2000,x)
    transit1 = MVNE_classic_transitions(start_time,2000,y)
    transit3 = MVNE_classic_transitions(start_time,2000,text.text)
    transit3.fadein()
    bg.showimg()
    fg.showimg()
    text.show_bbox()
    text.show_text()


    pygame.display.update()
    clock.tick(60)




pygame.quit()