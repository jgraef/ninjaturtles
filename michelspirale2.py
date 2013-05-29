from ninjaturtles import NinjaTurtle
from turtle import*
import pygame
from baum import ast
from math import sin,cos,tan



K=42
M=40
N=50000
Z=0.0000001

def farbe(t, n):
    c = pygame.Color(0, 0, 0)
    c.hsva = (int(sin(0.001*n)*180+180),  100, 100, 0)
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
        t.forward(50+i)
        t.left(cos(i))
        t.forward(-i*i)
        t.right(cos(i)+3)
    t.left(90)
    t.forwards(90)



if (__name__=="__main__"):
    t = NinjaTurtle((1280,1024))
    t.set_width(0.001)
    t.set_zoom(Z)
    spirale2(t)
    t.reset()
    #ast(t, 1, 1, 0)

t.screenshot()
