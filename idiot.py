import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

def draw_square(x, y, size, color,sizex,sizey):
    # Define the 4 vertices of the square
    vertices = [
        [x, y],
        [x + size, y],
        [x + size, y + size],
        [x, y + size]
    ]
    
    # Set OpenGL parameters
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, sizex*size, 0, sizey*size)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set square color
    glColor3f(*color)

    # Draw the square
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

# Initialize pygame
images = input("Enter the name of the image file: ")
scale = int(input("Enter the scale of the image: "))
pygame.init()
im = Image.open(images) # Can be many different formats.
pix = im.load()


print(im.size)  # Get the width and hight of the image for iterating over
# Set display parameters
display = (im.size[0]*scale, im.size[1]*scale)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    # Draw squares
    posx=0
    posy=0
    for i in range(im.size[0]):
        for j in range(im.size[1]-1,0,-1):
            print(pix[i,j][0]/256, pix[i,j][1]/256, pix[i,j][2]/256)
            draw_square(posy, posx, scale, (pix[i,j][0]/256, pix[i,j][1]/256, pix[i,j][2]/256),im.size[0],im.size[1])
            posx+=scale
        posy+=scale
        posx=0
    
    pygame.display.flip()
    pygame.time.wait(10)
