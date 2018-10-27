from src.gui.image_manager import ImageManger

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMainWindow, QFrame

from PyQt5.QtCore import Qt
import PyQt5.QtMultimedia
import PyQt5.QtGui

import PyQt5


class ImageWidget(QLabel):
    def __init__(self, img, parent=None):
        super(ImageWidget, self).__init__(parent)
        pixmap = PyQt5.QtGui.QPixmap(img)
        self.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())


class GuiWindow(QMainWindow):

    def __init__(self, controller, base_img_fp: str):
        super(GuiWindow, self).__init__()
        # self.app = QApplication([])

        self.img_manager = ImageManger(base_img_fp)

        self.controller = controller
        self.create_content()
        self.show()

    def create_content(self):
        self.snap_sound = PyQt5.QtMultimedia.QSound("snap_ex.wav")

        # Build the components first

        self.outer_widget = PyQt5.QtWidgets.QWidget(self)  # Dummy outer widget needed so that we can add others to it

        # This is the frame to hold the options.
        self.main_frame = PyQt5.QtWidgets.QGroupBox(self.outer_widget)  # Specifying parent=self locks it within the current window
        # self.main_frame.setTitle("Parameters")

        # The main layout for the param box and the image
        self.main_layout_wide = QHBoxLayout(self.main_frame)

        self.input_frame = QWidget(self.outer_widget)

        self.main_layout_wide.addWidget(self.input_frame)

        self.input_frame_layout = QVBoxLayout(self.input_frame)

        # Now, adding the parts back in...

        self.gain_slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal, self.input_frame)

        self.go_button = PyQt5.QtWidgets.QPushButton("*snap*", self.input_frame)

        self.go_button.clicked.connect(self.on_click)

        self.input_frame_layout.addWidget(self.gain_slider)
        self.input_frame_layout.addWidget(self.go_button)

        # Trying something else out

        self.image_frame = QFrame(self)

        # Creating the second container

        self.image_widget = ImageWidget("kju.jpg", self.outer_widget)

        self.main_layout_wide.addWidget(self.image_widget)

        # self.main_layout.addLayout(self.main_frame)

        self.setCentralWidget(self.outer_widget)

        self.setFixedSize(self.main_layout_wide.sizeHint())

        # self.main_frame.show()

    def on_click(self):
        self.snap_sound.play()

    def reload_image(self):
        """
        Reload the image within the current frame, asking the underlying functions to recalculate
        based on its current values.
        """
        img = self.img_manager.update_image()

        q_image = PyQt5.QtGui.QImage.fromData(img)
        q_pixmap = PyQt5.QtGui.QPixmap.fromImage(q_image)

        self.image_widget.setPixmap(q_pixmap)

    def on_slider_adjust(self):
        new_value = self.gain_slider.value()
        # TODO Scale this
        self.img_manager.gain = new_value


if __name__ == '__main__':
    app = QApplication([])

    g = GuiWindow(app, "kju.jpg")

    app.exit(app.exec_())
