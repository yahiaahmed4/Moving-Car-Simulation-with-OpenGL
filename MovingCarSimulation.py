from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np
from PIL import Image
import texture
import pygame

car_x = 0
car2_x = -500
car3_x= -1000
cloud_dir="right"
car_direction = "right"
car2_direction = "right"
car3_direction = "right"
signal_color = "green"
car_direction = "right"
color = (0.0,0.0,0.0)
color2=(1,1,0)
color3 =(0.53, 0.81, 0.92)
color4=(1,1,1)
pColor=(1,0,0)
greencolor=(0,1,0)
redcolor=(0,0,0)
cloud_x=475
cloud2_x=1075
pX=1000
pY=600
pX2=1130
pY2=630
state="morning"


def myInit():
    global buliding_tex
    glClearColor(0,0,0.0,1.0)
    glColor3f(0.0,0.0,0.0)
    glPointSize(2)
    gluOrtho2D(0,1500,0,750)
    
    # texture init
    buliding_tex = texture.Texture(img="home.jpg")
    # enable anti-aliasing
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)

   
def draw_buliding_tex(x1,y1,x2,y2,x3,y3,x4,y4):
    glActiveTexture(GL_TEXTURE0)
    # background texture
    buliding_tex.bindTexture()
    glColor(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    texture.texture_coord_map(0, 0, x1, y1)
    texture.texture_coord_map(1, 0, x2, y2)
    texture.texture_coord_map(1, 1, x3, y3)
    texture.texture_coord_map(0, 1, x4, y4)
    glEnd()
    glDisable(GL_TEXTURE_2D)  

def draw_quad(a,b,c,d,e,f,g,h,i,j,k):
    glBegin(GL_QUADS)
    glColor3f(a,b,c)
    glVertex2f(d,e)
    glVertex2f(f,g)
    glVertex2f(h,i)
    glVertex2f(j,k)
    glEnd()

def draw_polygon(a,b,c,d,e,f,g,h,i,j,k,l,m,n=0,o=0,p=0,q=0,r=0,s=0):
    glColor3f(a,b,c)
    glBegin(GL_POLYGON)
    glVertex2f(d,e)
    glVertex2f(f,g)
    glVertex2f(h,i)
    glVertex2f(j,k)
    glVertex2f(l,m)
    if n != 0 and o != 0:
        glVertex2f(n,o)
    if p != 0 and q !=0:
        glVertex2f(p,q)
    if r != 0 and s != 0:
        glVertex2f(r,s)
    glEnd()
    
def draw_triangle(a,b,c,d,e,f,g,h,i):
        glColor3f(a,b,c)
        glBegin(GL_TRIANGLES)
        glVertex2f(d,e)
        glVertex2f(f,g)
        glVertex2f(h,i)
        glEnd()

def draw_circle(a,b,c,d,e,f):
        glBegin(GL_POLYGON)
        glColor3f(a,b,c)
        x_centre = d
        y_centre = e
        r_inner = f
        num_segments = 20  # number of segments to approximate the circle
        for i in range(num_segments):
            angle = 2.0 * math.pi * i / num_segments
            x = r_inner * math.cos(angle) + x_centre
            y = r_inner * math.sin(angle) + y_centre
            glVertex2f(x,y)
        glEnd()
#motion of car
def update_cars():
    global car_x, car_direction, car2_x, car2_direction, car3_x, car3_direction

    if car_direction != "stop":
        car_x += 0.4  # Speed of the first car
        if car_direction == "right":
            if car_x >= 1250:
                car_x = -450
        else:
            if car_x <= -450:
                car_x = 1250

    if car2_direction != "stop":
        car2_x += 0.4  # Speed of the second car
        if car2_direction == "right":
            if car2_x >= 1250:
                car2_x = -450
        else:
            if car2_x <= -450:
                car2_x = 1250

    if car3_direction != "stop":
        car3_x += 0.4  # Speed of the third car
        if car3_direction == "right":
            if car3_x >= 1250:
                car3_x = -450
        else:
            if car3_x <= -450:
                car3_x = 1250

def update_plane():
    global plane_direction,pX,pX2,pY,pY2,state
    pXspeed = 0.6
    pYspeed = 0.2
    if state=="morning":
        pX,pY,pX2,pY2 = update_plane_position(pX,pX2,pY,pY2,pXspeed,pYspeed)
        
    elif state=="night":
        pX = 2000
        pX2= 2130
        pY=6000
        pY2=6030
        

def update_plane_position(x,x2,y,y2, xspeed,yspeed):
    if state=="morning":
        x-= xspeed
        x2-= xspeed
        y+=yspeed
        y2+=yspeed
        if y >= 800:
            x = 1000
            x2=1130
            y=600
            y2=630
   
    return x,y,x2,y2

def update_clouds():
    global cloud_x,cloud2_x,cloud_dir,state
    cloudspeed = 0.4
    if state=="morning":
        if cloud_x!=cloud2_x:
            cloud_x = update_cloud_position(cloud_x, cloud_dir, cloudspeed)
            cloud2_x = update_cloud_position(cloud2_x, cloud_dir, cloudspeed)
        else:
            cloud_x=400
            cloud2_x=1000
    elif state=="night":
        cloud_x=4705
        cloud2_x=4000

def update_cloud_position(x, direction, speed):
    x += speed
    if x >= 1500:
        x = 400
    return x


def idle():
    update_cars()
    update_plane()
    update_clouds()
    
    glutPostRedisplay()

def draw_windows(home_x, home_y, num_rows, num_cols, window_width, window_height, window_margin):
    for row in range(num_rows):
        for col in range(num_cols):
            window_x = home_x + (window_width + window_margin) * col
            window_y = home_y + (window_height + window_margin) * row
            draw_quad(*color3, window_x, window_y, window_x + window_width, window_y, window_x + window_width, window_y + window_height, window_x, window_y + window_height)

def keyboard(key, x, y):
    global signal_color, car_direction, car2_direction, car3_direction,color,color2,color3,greencolor,redcolor,color4,state,pColor
    if key == b'r':
        signal_color = "red"
        car_direction = "stop"
        car2_direction = "stop"
        car3_direction = "stop"
        redcolor=(1,0,0)
        greencolor=(0,0,0)

    elif key == b'g':
        signal_color = "green"
        car_direction = "right"
        car2_direction = "right"
        car3_direction = "right"
        redcolor=(0,0,0)
        greencolor=(0,1,0)
    elif key == b'w':
        state="morning"
        color = (0.53, 0.81, 0.92)  # Change color to white
        color2=(1,1,0)
        color3 = (0.53, 0.81, 0.92)
        color4=(1,1,1)
        pColor=(1,0,0)  #plane color
        glDisable(GL_LIGHTING)  # Disable lighting
        glDisable(GL_LIGHT0)  # Disable light source 0
        glDisable(GL_COLOR_MATERIAL)  # Disable material color tracking
    elif key == b'b':
        state="night"
        color = (0.0, 0.0, 0.0)
        color2 = (1,1,1)
        color3 = (0, 0, 0)
        color4=(0,0,0)
        pColor=(0,0,0)
        glEnable(GL_LIGHTING)  # Enable lighting
        glEnable(GL_LIGHT0)  # Enable light source 0
        glEnable(GL_COLOR_MATERIAL)  # Enable material color tracking

    glutPostRedisplay()

def draw_signal():
    global signal_color

    if signal_color == "green":
        glColor3f(0.0, 1.0, 0.0)
    else:
        glColor3f(1.0, 0.0, 0.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

        # Set up the light source properties
    light_position = (100.0, 700.0, 1.0, 1.0)  # Light position (x, y, z, w)
    light_diffuse = (1, 1, 1.0, 1.0)  # Light diffuse color (r, g, b, a)
    light_specular = (1, 1, 1.0, 1.0)  # Light specular color (r, g, b, a)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Set up the material properties
    material_diffuse = (1, 1, 1, 1.0)  # Material diffuse color (r, g, b, a)
    material_specular = (1, 1, 1, 1.0)  # Material specular color (r, g, b, a)
    material_shininess = 10.0  # Material shininess

    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, material_shininess)



    #sky
    draw_quad(*color3,0,0,1500,0,1500,750,0,750)
    #street
    draw_quad(0.5,0.5,0.8,0,0,1500,0,1500,125,0,125)
    #rasef
    draw_quad(0.5,0.5,0.5,0,125,1500,125,1500,225,0,225)
    #zar3
    draw_quad(0,0.4,0,0,225,1500,225,1500,450,0,450)
    #sun
    draw_circle(*color2,150,675,50)
    #tree
    draw_quad(0.6,0.4,0.2,525,300,550,300,550,378,525,378)
    draw_circle(0,1,0,510,387,32)
    draw_circle(0,1,0,560,387,32)
    draw_circle(0,1,0,550,435,32)
    draw_circle(0,1,0,535,475,27)
    draw_circle(0,1,0,520,435,32)
    #window home 1
    #home 1
    draw_polygon(0.2,0.2,0.8,50,225,175,225,200,250,200,550,175,575,50,575)
    draw_quad(*color3,87,225,125,225,125,287,87,287)
    draw_windows(62,330,4,2,35,35,30)
    #window home 2
    #home 2
    draw_polygon(1,0,0,225,225,425,225,450,250,450,475,425,500,225,500)
    draw_quad(*color3,300,225,350,225,350,287,300,287)
    draw_windows(250,330,3,2,55,30,25)
    #window home 3
    #home 3
    draw_polygon(1,1,0,600,225,725,225,750,250,750,550,725,575,600,575)
    draw_quad(*color3,640,225,685,225,685,287,640,287)
    draw_windows(605,330,4,3,30,40,20)
    #home4
    draw_quad(0,1,1,775,225,875,225,875,600,775,600)
    draw_triangle(0,1,1,775,600,875,600,825,650)
    draw_triangle(0,1,1,820,645,830,645,825,700)
    draw_quad(*color3,800,225,850,225,850,350,800,350)
    draw_quad(*color3,790,440,860,440,860,550,790,550)
    #home 5
    draw_buliding_tex(900,225,1200,225,1200,500,900,500)
    # draw_quad(0,1,0,900,225,1200,225,1200,500,900,500)
    # draw_quad(*color3,1000,225,1100,225,1100,300,1000,300)
    # draw_windows(910,330,2,4,55,55,20)
    #home 6
    draw_polygon(0.4,0.6,0.1,1200,225,1400,225,1425,250,1425,550,1400,575,1200,575)
    draw_windows(1262.5,225,1,1,70,70,0)
    draw_windows(1225,330,4,3,35,35,20)
    #sa7aba1
    draw_circle(*color4,cloud_x,650,40)
    draw_circle(*color4,cloud_x+50,625,40)
    draw_circle(*color4,cloud_x+50,675,40)
    draw_circle(*color4,cloud_x+100,650,40)
    #sa7aba2
    draw_circle(*color4,cloud2_x,650,40)
    draw_circle(*color4,cloud2_x+50,625,40)
    draw_circle(*color4,cloud2_x+50,675,40)
    draw_circle(*color4,cloud2_x+100,650,40)
    #3amod nor
    draw_quad(0,0,0,460,275,475,275,475,137,460,137)
    draw_triangle(0,0,0,460,275,500,275,480,300)
    draw_quad(1,1,1,480,220,495,220,495,275,480,275)

    #plane
    draw_quad(*pColor,pX,pY,pX+50,pY+30,pX+170,pY+30,pX+100,pY)
    draw_quad(*pColor,pX2,pY2,pX2+30,pY2+70,pX2+50,pY2+70,pX2+40,pY2)




    #car1
    draw_polygon(1, 0, 0, 400 + car_x, 25, 850 + car_x, 25, 825 + car_x, 90, 770 + car_x, 100, 740 + car_x, 180, 510 + car_x, 180, 475 + car_x, 100, 400 + car_x, 75)
    draw_circle(0,0,0, 525 + car_x, 25, 25)
    draw_circle(0, 0, 0, 725 + car_x, 25, 25)
    draw_quad(*color3, 500 + car_x, 100, 600 + car_x, 100, 600 + car_x, 150, 525 + car_x, 150)
    draw_quad(*color3, 625 + car_x, 100, 750 + car_x, 100, 720 + car_x, 150, 625 + car_x, 150)
    # car2
    draw_polygon(0, 1, 0, 400 + car2_x, 25, 850 + car2_x, 25, 850 + car2_x, 100, 830 + car2_x, 220, 400 + car2_x, 220)
    draw_circle(0, 0, 0, 525 + car2_x, 25, 25) 
    draw_circle(0, 0, 0, 725 + car2_x, 25, 25)
    draw_windows(420+car2_x,150,1,4,50,50,30)
    draw_quad(*color3, 770 + car2_x, 150, 835 + car2_x, 150, 825 + car2_x, 210, 770 + car2_x, 210)
    draw_quad(*color3,760+car2_x,30,car2_x+820,30,car2_x+820,130,car2_x+760,130) #door

    #car 3
    draw_polygon(1, 1, 0, 400 + car3_x, 25, 850 + car3_x, 25, 825 + car3_x, 90, 770 + car3_x, 100, 740 + car3_x, 180, 510 + car3_x, 180, 475 + car3_x, 100, 400 + car3_x, 75)
    draw_circle(0, 0, 0, 525 + car3_x, 25, 25)
    draw_circle(0, 0, 0, 725 + car3_x, 25, 25)
    draw_quad(*color3, 500 + car3_x, 100, 600 + car3_x, 100, 600 + car3_x, 150, 525 + car3_x, 150)
    draw_quad(*color3, 625 + car3_x, 100, 750 + car3_x, 100, 720 + car3_x, 150, 625 + car3_x, 150)
    #traffic_signal
    draw_quad(0,0,0,1465,200,1475,200,1475,450,1465,450)
    draw_quad(0.5,1,1,1440,300,1500,300,1500,450,1440,450)
    draw_circle(*redcolor,1470,425,25)
    draw_circle(1,1,0,1470,375,25)
    draw_circle(*greencolor,1470,325,25)

    
   
    draw_signal()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1500, 750)
glutCreateWindow("Moving Car")
glMatrixMode(GL_PROJECTION)
glutDisplayFunc(display)

glutKeyboardFunc(keyboard)
myInit() 
glutIdleFunc(idle)
glutMainLoop()