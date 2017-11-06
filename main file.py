import turtle

from myShape import *

from random import randint
turtle.colormode (255)
turtle.bgcolor (0, 49, 125)
turtle.tracer (0)
bob=turtle.Turtle ()

for times in range (500):
    a= randint (-800,800)
    s= randint (-800,800)
    n = randint (1,5)
    b= randint (100,255)
    r=randint (100,255)
    e=randint (100,255)

    bob.color (b,r,e)
    
    rainbowsnow (bob,n,a,s)

bob.width (10)
    
for times in range (55):
    
    supernova (bob)
