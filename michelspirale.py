from ninjaturtles import NinjaTurtle
import pygame
from baum import ast
from math import sin,cos



K=42
M=40
N=5000


def farbe(t, n):
    c = pygame.Color(0, 0, 0)
    c.hsva = (int((1-(n+1)/N) * 360.0), 100, 100, 0)
    t.set_color(c.r/255, c.g/255, c.b/255)


def spirale(t):
    t.set_pos((20,0))
    for i in range(N):
        farbe(t,i)
        for j in range(360):
            t.left(0.5)
            t.forward(sin(i)+0.1)
        t.up()
        t.forward(i+10)
        t.left(1)
        t.down()

def spirale2(t):
    for i in range (N):
        farbe(t,i)
        t.forward(1+i)
        t.left(90-i)

if (__name__=="__main__"):
    t = NinjaTurtle((1280,1024))
    t.set_width(2)
    t.set_zoom(0.01)
    spirale2(t)
    t.reset()
    #ast(t, 1, 1, 0)

t.screenshot()
