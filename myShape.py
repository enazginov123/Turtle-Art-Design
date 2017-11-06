def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(90)

def triangle (t, distance):
   for times in range(3):
        t.forward (distance)
        t.left (120)




def pentagon (t, distance):
    angle= 360/5
    
    for times in range(5):
        t.forward (distance)
        t.left (angle)
def polygon (t,distance, side):
    angle= 360/side
    t.begin_fill ()
    for times in range (side):
        t.forward (distance)
        t.left (angle)
        t.end_fill ()

def star (t,distance):
   
   
   
    for time in range (4):
        t.forward (distance)
        t.left (135)



def stars (t,distance):
   
   for time in range (4):
        t.forward (distance)
        t.left (135)




    
    


def move (t,x,y):
    t.penup ()
    t.goto (x,y)
    t.pendown ()

def eraser (t,x,y):
    for times in range (5):
        t.color (0,0,0)
        t.width (200)
        t.penup ()
        t.goto (x,y)
        t. pendown ()
        t.forward (100)
        t.left (90)
def flower (t,distance, side):
    
   
    for times in range (side):
       
        t.forward (distance)
        t.left (120)

        
def rainbowsnow (t,size,x,y):
        move (t,x,y)
        t.begin_fill ()
        t. color ()
        t.circle (size)
        t.end_fill ()


def stripes (t, size):
    move (t, -800,-400)
    for times in range (30):
        polygon (t, size, 4)
        t.forward (150)


def supernova (t):
    angle= 1
    t.begin_fill ()
    move (t,0,0)
 
    t.color (0,255,255)
    stars (t,350)
    t.left (angle)
    t.color (0,255,0)
    stars (t,300)
    t.left (angle)
    t.color (0,0,255)
    stars (t,250)
    t.left (angle)
    t.color (90,230,255)
    stars (t,200)
    t.left (angle)
    t.color (255,0,0)
    stars (t,150)
    t.left (angle)
    t.color (246,30,90)
    stars (t,100)
    t.left (angle)
    t.color (8,255,60)
    stars (t,50)
    t.left (angle)
    t.color (255,255,255)
    t.end_fill ()


def an (t):
    angle= 360
    t.begin_fill ()
    move (t,0,0)
    t.color (255,0,0)
    star (t,500)
    t.left (angle)
    t.color (255,0,255)
    star (t,450)
    t.left (angle)
    t.color (255,255,0)
    star (t,400)
    t.left (angle)
    t.color (0,255,255)
    star (t,350)
    t.left (angle)
    t.color (0,255,0)
    star (t,300)
    t.left (angle)
    t.color (0,0,255)
    star (t,250)
    t.left (angle)
    t.color (90,230,255)
    star (t,200)
    t.left (angle)
    t.color (255,0,0)
    star (t,150)
    t.left (angle)
    t.color (246,30,90)
    star (t,25)
    t.left (angle)
    t.color (8,255,60)
    star (t,2)
    t.left (angle)
    t.color (255,255,255)
    t.end_fill ()

def smallstars (t,size,x,y):
        move (t,x,y)
        t.begin_fill ()
        t. color (255,255,0)
        t.circle (size)
        t.end_fill ()


def clock (t):
    angle = 1
    t.begin_fill()
    
    move (t,0,0)
    star (t,500)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,450)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,400)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,350)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,300)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,250)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,200)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,150)
    t.left (angle)
    t.fillcolor (255,0,0)
    star (t,100)
    t.color (255,0,255)
    t.end_fill


def supernova2 (t):
    distance = 1
    angle= 1
    t.begin_fill ()
    move (t,0,0)
    t.color (255,0,0)
    star (t,500)
    t.left (angle)
    t.forward (distance)
    t.color (255,0,255)
    star (t,450)
    t.left (angle)
    t.forward (distance)
    t.color (255,255,0)
    star (t,400)
    t.left (angle)
    t.forward (distance)
    t.color (0,255,255)
    star (t,350)
    t.left (angle)
    t.forward (distance)
    t.color (0,255,0)
    star (t,300)
    t.left (angle)
    t.forward (distance)
    t.color (0,0,255)
    star (t,250)
    t.left (angle)
    t.forward (distance)
    t.color (90,230,255)
    star (t,200)
    t.left (angle)
    t.forward (distance)
    t.color (255,0,0)
    star (t,150)
    t.left (angle)
    t.forward (distance)
    t.color (246,30,90)
    star (t,100)
    t.left (angle)
    t.forward (distance)
    t.color (8,255,60)
    star (t,50)
    t.left (angle)
    t.forward (distance)
    t.color (255,255,255)
    t.end_fill ()
