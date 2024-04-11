from tkinter import *
from tkinter import messagebox
from threading import Thread
from random import randint
from PIL import Image
from time import sleep



#pop up
def spam(mycolor,posx,posy):

    mibox = Tk()
    topframe = Frame(mibox)
    topframe.pack()
    mibox.geometry("10x10+"+str(posx)+"+"+str(posy))
    mibox.configure(bg=mycolor)
    mibox.overrideredirect(True)
    mibox.mainloop()

    #do something here
im = Image.open('mgrbig.png') # Can be many different formats.
pix = im.load()

posx=0
posy=0
print(im.size)  # Get the width and hight of the image for iterating over
for i in range(im.size[0]):
    for j in range(im.size[1]):
        try:
            mycolor = '#%02x%02x%02x' % (pix[i,j][0], pix[i,j][1], pix[i,j][2])  # set your favourite rgb color
        except:
            mycolor = '#000000'
        # print(mycolor,posx,posy)  # Get the RGBA Value of the a pixel of an image
        Thread (target=spam,args=(mycolor,posx,posy)).start()
        posx+=10
    posy+=10
    posx=0

while(1):
    {

    }