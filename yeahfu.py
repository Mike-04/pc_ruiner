from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QImage
from PyQt5.QtCore import QTimer, Qt
from PIL import Image
import random
import sys
import os

class ShittyImageViewer(QWidget):
    def __init__(self, base_image_path, overlay_image_path):
        super().__init__()
        self.base_image_path = base_image_path
        self.overlay_image_path = overlay_image_path

        self.base_image = Image.open(base_image_path)
        self.qimage_base = QImage(base_image_path)

        # Resize the overlay image to match the base image size
        self.overlay_image = Image.open(overlay_image_path).resize((self.qimage_base.width(), self.qimage_base.height()))
        self.qimage_overlay = QImage(self.overlay_image_path).scaled(self.qimage_base.size(), Qt.KeepAspectRatio)

        self.setWindowTitle('Shitty Image Viewer')
        self.setGeometry(100, 100, self.qimage_base.width(), self.qimage_base.height())
        #disable resizing
        self.setFixedSize(self.qimage_base.width(), self.qimage_base.height())
        self.image_visible = True  # To manage the visibility state of the original image

        self.total_pixels = self.qimage_base.width() * self.qimage_base.height()
        self.drawn = 0
        self.pixels = [[0 for x in range(self.qimage_base.width())] for y in range(self.qimage_base.height())]
        self.pixel_list = [(x, y) for x in range(self.qimage_base.width()) for y in range(self.qimage_base.height())]
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
        # Draw the base image
        painter.drawImage(self.rect(), self.qimage_base)
        if not self.image_visible:
            # Draw random colored pixels from the overlay image over the base image
            for y in range(self.qimage_base.height()):
                for x in range(self.qimage_base.width()):
                    if self.pixels[y][x] == 1:
                        overlay_color = self.overlay_image.getpixel((x, y))
                        painter.setPen(QColor(overlay_color[0], overlay_color[1], overlay_color[2]))
                        painter.drawPoint(x, y)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_dir = os.path.expanduser("~")
    downloads_dir = os.path.join(home_dir, "Downloads")
    
    base_filename, _ = QFileDialog.getOpenFileName(None, "Select the base image", downloads_dir, "Image Files (*.png *.jpg *.bmp)")
    if base_filename:
        # Specify the overlay image path relative to the script location
        script_dir = os.path.dirname(os.path.realpath(__file__))
        overlay_filename = os.path.join(script_dir, "overlay_image.jpg")
        
        if os.path.exists(overlay_filename):
            window = ShittyImageViewer(base_filename, overlay_filename)
            window.resize(window.qimage_base.size())
            window.show()
            sys.exit(app.exec_())
        else:
            print(f"Overlay image not found at: {overlay_filename}")
            sys.exit()
    else:
        sys.exit()
