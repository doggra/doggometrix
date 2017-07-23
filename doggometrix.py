#!/usr/bin/env python
# Import a library of functions called 'pygame'
import pygame
from math import pi, sin, cos, radians

SCREENW = 1280
SCREENH = 1024

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (118, 255,   3)
RED =   (255,   0,   0)

pygame.init()
clock = pygame.time.Clock()
clock.tick(1)

size = [SCREENW, SCREENH]
done = False
pause = False
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption("Doggometrix")

side_length = 800
h_side_length = side_length/2

# # Starting point (center)
x = size[0]/2 - h_side_length
y = size[1]/2 - h_side_length

pl = [ [x, y], [x+side_length, y], [x+side_length, y+side_length], [x, y+side_length] ]


def draw_polygon(pl):
    poly = pygame.draw.polygon(SCREEN, WHITE, pl, 1)


def move_on_vector(x1, y1, x2, y2, dist=10):
    new_x = x1+(x2-x1)/dist
    new_y = y1+(y2-y1)/dist
    return [new_x, new_y]


while not done:
    clock.tick(10)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done= True

            if event.key == pygame.K_q:
                done= True

            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.key == pygame.K_p:
                pause = True if pause == False else False

        if event.type == pygame.QUIT:
            done=True
 
    if not pause:
        draw_polygon(pl)

        p1 = pl[0]
        p2 = pl[1]
        p3 = pl[2]
        p4 = pl[3]

        # Update coordinates
        pl = [ move_on_vector(p1[0], p1[1], p2[0], p2[1]), 
               move_on_vector(p2[0], p2[1], p3[0], p3[1]),
               move_on_vector(p3[0], p3[1], p4[0], p4[1]),
               move_on_vector(p4[0], p4[1], p1[0], p1[1])]

        # # Reverse rotation
        #
        # pl = [ move_on_vector(p2[0], p2[1], p1[0], p1[1]), 
        #        move_on_vector(p3[0], p3[1], p2[0], p2[1]),
        #        move_on_vector(p4[0], p4[1], p3[0], p3[1]),
        #        move_on_vector(p1[0], p1[1], p4[0], p4[1])]


    pygame.display.flip()
     
# Be IDLE friendly
pygame.quit()