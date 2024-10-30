from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QImage
from PyQt5.QtCore import QTimer, Qt
from PIL import Image
import random
import sys

class ShittyImageViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.qimage = QImage(self.image_path)
        self.setWindowTitle("Image Unviewer")
        self.setGeometry(100, 100, self.qimage.width(), self.qimage.height())
        self.image_visible = True  # To manage the visibility state of the original image

        self.total_pixels = self.qimage.width() * self.qimage.height()
        self.drawn = 0
        self.pixels = [[0 for x in range(self.qimage.width())] for y in range(self.qimage.height())]
        self.pixel_list = [(x, y) for x in range(self.qimage.width()) for y in range(self.qimage.height())]
        random.shuffle(self.pixel_list)  # Shuffle the pixel list to ensure randomness

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(500)  # Show the image for 2 seconds before starting the redraw

    def update_image(self):
        if self.image_visible:
            self.image_visible = False
            self.timer.start(1)  # Update every 10 ms for redrawing
        else:
            if self.drawn < self.total_pixels:
                # Draw a batch of 100 pixels at each timer tick
                for _ in range(10000):
                    if self.drawn < self.total_pixels:
                        x, y = self.pixel_list[self.drawn]
                        self.pixels[y][x] = 1
                        self.drawn += 1
                self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        # Draw the original image
        painter.drawImage(self.rect(), self.qimage)
        if not self.image_visible:
            # Draw random colored pixels over the original image
            for y in range(self.qimage.height()):
                for x in range(self.qimage.width()):
                    if self.pixels[y][x] == 1:
                        painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                        painter.drawPoint(x, y)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filename, _ = QFileDialog.getOpenFileName(None, "Select an image", "", "Image Files (*.png *.jpg *.bmp)")
    if filename:
        window = ShittyImageViewer(filename)
        window.resize(window.qimage.size())
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()
