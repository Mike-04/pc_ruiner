from tkinter import *
from tkinter import messagebox
from threading import Thread
from random import randint


spamreturn = False

def something_doer():
    val = 0
    while True:
        val += 1
        if val > 1000000:
            print("done")
            val=0

#pop up
def spam():

    mibox = Tk()
    topframe = Frame(mibox)
    miLabel = Label(mibox, text="Your PC is doing something weird...")
    mibutton2 = Button(topframe, text="OH well what can I do?")
    miLabel.pack()
    mibutton2.pack()
    topframe.pack()
    x=randint(0,1920)
    y=randint(0,1080)
    mibox.geometry("300x100+"+str(x)+"+"+str(y))

    mibox.protocol("WM_DELETE_WINDOW")

    idiot = Thread(target=something_doer)
    idiot.start()

    mibox.mainloop()

    #do something here

        


for i in range(10000):
    t = Thread(target=spam)
    t.start()
