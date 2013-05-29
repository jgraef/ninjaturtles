from ninjaturtles import NinjaTurtle
from time import time
from random import uniform

N=17

def farbe(t, n):
    t.set_color(1-n/N, n/N, 0.1)

def ast(t, n, i,m):
    if n==N:
        return
    
    farbe(t, n)
    #astlänge = 100/(n*(i**0.2)) if m==0 else uniform(-10,+10)+70/(n*(i**0.2))
    astlänge = 100/(n*(i**0.2))
    astbreite = 0.5*(N-n)
    t.set_width(astbreite)
    t.forward(astlänge)

    t.left(30)
    ast(t, n+1, i,0)
    t.right(60)
    ast(t, n+1, i,1)
    t.left(30)

    farbe(t, n)
    t.set_width(astbreite)
    t.backward(astlänge)


if (__name__=="__main__"):
    t = NinjaTurtle((1024, 768))
    i = 1
    t.set_zoom(1.0)
    ast(t, 1, 1, 0)
    t.right(45)
    i += 1

