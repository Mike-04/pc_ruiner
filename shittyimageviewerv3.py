from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QImage
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
import random
import sys
import math

class ImageWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.qimage = QImage(self.image_path)
        self.setWindowTitle('Shitty Image Viewer')
        self.setGeometry(100, 100, self.qimage.width(), self.qimage.height())
        
        self.total_pixels = self.qimage.width() * self.qimage.height()
        self.drawn = 0
        self.pixels = [[0 for x in range(self.qimage.width())] for y in range(self.qimage.height())]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_line)
        self.timer.start(10)  # Update every 10 ms

    def update_line(self):
        if self.drawn < self.total_pixels:
            for _ in range(10):  # Adjust this number to control the speed of drawing
                x = random.randint(0, self.qimage.width() - 1)
                y = random.randint(0, self.qimage.height() - 1)
                self.draw_circle(x, y, 10)  # Draw a circle of radius 10 pixels
            self.update()

    def draw_circle(self, cx, cy, radius):
        for y in range(max(0, cy - radius), min(self.qimage.height(), cy + radius)):
            for x in range(max(0, cx - radius), min(self.qimage.width(), cx + radius)):
                if (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2 and self.pixels[y][x] == 0:
                    self.pixels[y][x] = 1
                    self.drawn += 1

    def paintEvent(self, event):
        painter = QPainter(self)
        for y in range(self.qimage.height()):
            for x in range(self.qimage.width()):
                if self.pixels[y][x] == 1:
                    color = self.qimage.pixelColor(x, y)
                    painter.setPen(QColor(color.red(), color.green(), color.blue()))
                    painter.drawPoint(x, y)
        painter.end()

    def resizeEvent(self, event):
        new_size = event.size()
        self.qimage = self.qimage.scaled(new_size, Qt.KeepAspectRatio)
        self.update()  # Trigger a paint event
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filename, _ = QFileDialog.getOpenFileName(None, "Select an image", "", "Image Files (*.png *.jpg *.bmp)")
    if filename:
        window = ImageWidget(filename)
        window.resize(window.qimage.size())
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()
