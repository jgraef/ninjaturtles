from ninjaturtles import NinjaTurtle
from math import exp
import pygame


N = 20
RATIO = 1/1.45

def farbe(n):
    c = pygame.Color(0, 0, 0)
    c.hsva = (int(exp(n)/exp(N) * 360.0), 100, 100, 0)
    t.set_color(c.r/255, c.g/255, c.b/255)

def kurve(n):
    if (n>=N):
        return

    l = 10 / ((n+1)**RATIO)
    farbe(n)
    t.forward(l)
    
    t.right(45)
    kurve(n+1)
    t.left(90)
    kurve(n+1)
    t.right(45)
    

t = NinjaTurtle((1280, 1024))
t.set_zoom(0.1)
kurve(0)
