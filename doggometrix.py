#!/usr/bin/env python
# Import a library of functions called 'pygame'
import pygame
from math import pi, sin, cos, radians

FPS = 20
SCREENW = 1280
SCREENH = 1024

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = [118, 255,   3]
RED =   (255,   0,   0)

pygame.init()
clock = pygame.time.Clock()
clock.tick(1)

squares = triangles = []

# Running opts
running = True
pause = False
SCREENSIZE = [SCREENW, SCREENH]
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Doggometrix")

# Objects opts
color = start_color = [0,0,0]
stop_color = (244, 67, 54)
color_steps = 120.000

depth = 50
side_length = 2280
h_side_length = side_length/2
x = SCREENSIZE[0]/2 - h_side_length
y = SCREENSIZE[1]/2 - h_side_length


def move_on_vector(x1, y1, x2, y2, dist=5.00):
    new_x = x1+(x2-x1)/dist
    new_y = y1+(y2-y1)/dist
    return [new_x, new_y]
         

class NestedSquare(object):

    def __init__(self, pl=None, cr=[255,255,255]):
        super(NestedSquare, self).__init__()
        self.pl = pl
        self.color = cr
        self.poly = None

    def fractal_draw(self):
        self.draw()

    def draw(self):
        self.poly = pygame.draw.polygon(SCREEN, self.color, self.pl, 0)

    def update(self):

        p1 = self.pl[0]
        p2 = self.pl[1]
        p3 = self.pl[2]
        p4 = self.pl[3]
        self.pl = [move_on_vector(p1[0], p1[1], p2[0], p2[1]), 
                   move_on_vector(p2[0], p2[1], p3[0], p3[1]),
                   move_on_vector(p3[0], p3[1], p4[0], p4[1]),
                   move_on_vector(p4[0], p4[1], p1[0], p1[1])]


class NestedTriangle(object):

    def __init__(self, pl=None, cr=[255,255,255]):
        self.pl = pl
        self.color = cr
        self.poly = None

    def fractal_draw(self):
        self.draw()

    def draw(self):
        self.poly = pygame.draw.polygon(SCREEN, self.color, self.pl, 0)

start_square = [[x, y], 
                [x+side_length, y], 
                [x+side_length, y+side_length], 
                [x, y+side_length]]

start_triangle = [[x, y], 
                [x+side_length, y], 
                [x+side_length, y+side_length]]

pl = start_square
for i in xrange(depth):

    # Set color
    clr = []
    clr.append(int(color[0]+((stop_color[0] - color[0]) / color_steps)*i))
    clr.append(int(color[1]+((stop_color[1] - color[1]) / color_steps)*i))
    clr.append(int(color[2]+((stop_color[2] - color[2]) / color_steps)*i))
    color = clr

    # Add square
    ns = NestedSquare(pl, cr=clr)
    squares.append(ns)

    # Move on vector to next corner
    p1 = pl[0]
    p2 = pl[1]
    p3 = pl[2]
    p4 = pl[3]
    pl = [move_on_vector(p1[0], p1[1], p2[0], p2[1]), 
          move_on_vector(p2[0], p2[1], p3[0], p3[1]),
          move_on_vector(p3[0], p3[1], p4[0], p4[1]),
          move_on_vector(p4[0], p4[1], p1[0], p1[1])]

# color = start_color
# pl = start_triangle
# for i in xrange(depth):

#     # Set color
#     clr = []
#     clr.append(int(color[0]+((stop_color[0] - color[0]) / color_steps)*i))
#     clr.append(int(color[1]+((stop_color[1] - color[1]) / color_steps)*i))
#     clr.append(int(color[2]+((stop_color[2] - color[2]) / color_steps)*i))
#     color = clr

#     # Add triangle
#     nt = NestedTriangle(pl, cr=clr)
#     triangles.append(nt)

#     # Move on vector to next corner
#     p1 = pl[0]
#     p2 = pl[1]
#     p3 = pl[2]
#     pl = [move_on_vector(p1[0], p1[1], p2[0], p2[1]), 
#           move_on_vector(p2[0], p2[1], p3[0], p3[1]),
#           move_on_vector(p3[0], p3[1], p1[0], p1[1])]

# Start main loop
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.key == pygame.K_p:
                pause = True if pause == False else False

        if event.type == pygame.QUIT:
            running = False
 
    if not pause:
        SCREEN.fill(BLACK)

        for sq in squares:
            sq.fractal_draw()

        for tri in triangles:
            tri.fractal_draw()

        # # Reverse rotation
        #
        # pl = [ move_on_vector(p2[0], p2[1], p1[0], p1[1]), 
        #        move_on_vector(p3[0], p3[1], p2[0], p2[1]),
        #        move_on_vector(p4[0], p4[1], p3[0], p3[1]),
        #        move_on_vector(p1[0], p1[1], p4[0], p4[1])]


    pygame.display.flip()

pygame.quit()