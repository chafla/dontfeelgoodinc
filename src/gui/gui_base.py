from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

from PyQt5.QtCore import Qt
import PyQt5.QtMultimedia
import PyQt5.QtGui

import PyQt5


# app = QApplication([])
#
# # window = Q
#
# app.setStyleSheet("QPushButton { margin: 10ex; }")
#
# label = QLabel("ur mom gay")
#
# window = QWidget()
#
# layout = QVBoxLayout(window)
#
# button = QPushButton("click")
#
# def on_button_clicked():
#     alert = PyQt5.QtWidgets.QMessageBox()
#     alert.setText("Oof")
#     alert.exec_()
#
# button.clicked.connect(on_button_clicked)

# layout.addWidget(QPushButton("Top"))
# layout.addWidget(QPushButton("Me irl"))

# window.setLayout(layout)

# button.show()
#
# label.show()
# app.exec_()

class Gui:

    def __init__(self):
        self.snap_sound = PyQt5.QtMultimedia.QSound("snap_ex.wav")

        self.img = None

        # Boilerplate defs
        # Define the app
        self.app = QApplication([])

        self.window = PyQt5.QtWidgets.QMainWindow()
        self.window.show()

        self.true_central_widget = QHBoxLayout()

        self.central_widget = QWidget()

        # Image definition
        self.image_widget = QWidget()
        self.img = PyQt5.QtWidgets.QLabel(self.image_widget)
        pixmap = PyQt5.QtGui.QPixmap("kju.jpg")
        self.img.setPixmap(pixmap)
        self.img.resize(pixmap.width(), pixmap.height())
        self.image_widget.show()

        # self.add_image()

        self.left_col_layout = QVBoxLayout(self.central_widget)

        self.gain_slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal, self.central_widget)

        self.go_button = PyQt5.QtWidgets.QPushButton("*snap*", self.central_widget)

        self.left_col_layout.addWidget(self.gain_slider)
        self.left_col_layout.addWidget(self.go_button)

        self.true_central_widget.addWidget(self.central_widget)
        self.true_central_widget.addWidget(self.image_widget)

        self.central_widget.setLayout(self.true_central_widget)

        self.window.setCentralWidget(self.central_widget)

        self.img.show()

        self.window.show()

        # Register button to snap

        self.go_button.clicked.connect(self.on_click)



    def run(self):
        self.app.exit(self.app.exec_())

    def on_click(self):
        self.snap_sound.play()

    def add_image(self):
        pass


class ImageWidget(QWidget):
    def __init__(self, img, parent=None):
        super(ImageWidget, self).__init__(parent)

        self._img = img

        self.pixmap = QLabel(self)







g = Gui()
g.run()





