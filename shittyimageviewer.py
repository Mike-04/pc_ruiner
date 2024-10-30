#import qt painter
from PyQt5.QtWidgets import QWidget, QApplication , QFileDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect
#import image from pillow
from PIL import Image


# open a qt window to select an image
app = QApplication([])
filename, _ = QFileDialog.getOpenFileName(None, "Select an image", "", "Image Files (*.png *.jpg *.bmp)")
if not filename:
    exit()

print(filename)
#open a qt window with the image name


# create a qt window
window = QWidget()
window.setWindowTitle('Shitty Image Viewer')
#set the window size to the image size
window.show()

# create a qt painter
painter = QPainter()


# draw the image
def paintEvent(event):
    #get the windows size
    hight = window.height()
    width = window.width()
    #resize the image to the window size
    #if the image is too big it will be resized to fit 1000x1000
    
    im = Image.open(filename)
    im=im.resize((width,hight))

    #begin the painter


    painter.begin(window)
    #get all the pixels of the image
    pixels = im.load()
    #iterate over all the pixels
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            #set the color of the pixel
            painter.setPen(QColor(pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))
            #draw the pixel
            painter.drawPoint(i, j)
    painter.end()

window.paintEvent = paintEvent

# run the qt application
app.exec_()




