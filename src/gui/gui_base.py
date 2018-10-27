from PyQt5.QtGui import QMovie

from src.gui.image_manager import ImageManager
from src.gui.animation_ready_emitter import AnimationReadyEmitter

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMainWindow, QFrame

from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread
import PyQt5.QtMultimedia
import PyQt5.QtGui

from time import sleep

import PyQt5


class AnimationWidget(QWidget):

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)

        self.movie = QMovie(file_path)

        self.label = QLabel(self)
        self.label.setMovie(self.movie)

    def run(self):
        self.movie.start()


class AnimWorker(QObject):

    anim_done = pyqtSignal(str)

    def __init__(self, img_manager: ImageManager, override: bool):
        super().__init__()
        self._manager = img_manager
        self._override = override

    @pyqtSlot()
    def work(self):
        fp = "tmp.gif"
        # We could offload this to another thread
        self._manager.create_animation(fp)
        self.anim_done.emit(fp)


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

        self.img_manager = ImageManager(base_img_fp)

        self._anim_thread = None
        self._anim_worker = None
        self.animation_widget = None

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

        self.gain_slider_label = PyQt5.QtWidgets.QLabel(self.input_frame)
        self.gain_slider_label.setText("Gain")

        self.gain_slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal, self.input_frame)
        self.gain_slider.valueChanged.connect(self.on_gain_slider_adjust)

        # size slider

        self.chunk_slider_label = PyQt5.QtWidgets.QLabel(self.input_frame)
        self.chunk_slider_label.setText("Chunk size")

        self.chunk_size_slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal, self.input_frame)

        # This needs to be controlled with a single button press as it'll involve reloading the object
        self.chunk_size_button = PyQt5.QtWidgets.QPushButton("Apply chunk size", self.input_frame)

        self.chunk_size_button.clicked.connect(self.on_chunk_click)

        self.go_button = PyQt5.QtWidgets.QPushButton("*snap*", self.input_frame)

        self.go_button.clicked.connect(self.on_snap)

        self.full_snap_button = PyQt5.QtWidgets.QPushButton("Full snap", self.input_frame)

        self.full_snap_button.clicked.connect(self.display_animation)

        self.reset_button = PyQt5.QtWidgets.QPushButton("Use the time stone (reset)", self.input_frame)

        self.reset_button.clicked.connect(self.on_reset)

        self.input_frame_layout.addWidget(self.chunk_slider_label)
        self.input_frame_layout.addWidget(self.chunk_size_slider)
        self.input_frame_layout.addWidget(self.chunk_size_button)
        self.input_frame_layout.addWidget(self.gain_slider_label)
        self.input_frame_layout.addWidget(self.gain_slider)
        self.input_frame_layout.addWidget(self.go_button)
        self.input_frame_layout.addWidget(self.full_snap_button)
        self.input_frame_layout.addWidget(self.reset_button)

        # Trying something else out

        self.image_frame = QFrame(self)

        # Creating the second container

        self.image_widget = ImageWidget("kju.jpg", self.outer_widget)

        self.main_layout_wide.addWidget(self.image_widget)

        # self.main_layout.addLayout(self.main_frame)

        self.setCentralWidget(self.outer_widget)

        self.setFixedSize(self.main_layout_wide.sizeHint())

        # Make sure we're ready to handle an animation if the need arises
        # AnimationReadyEmitter.trigger.connect(self.display_animation)

        # self.main_frame.show()

    def display_animation(self):
        self._anim_worker = AnimWorker(self.img_manager, True)
        self._anim_thread = QThread()
        self._anim_worker.moveToThread(self._anim_thread)

        self._anim_worker.anim_done.connect(self.on_animation_complete)

        self._anim_thread.started.connect(self._anim_worker.work)
        self._anim_thread.start()

    @pyqtSlot(str)
    def on_animation_complete(self, file_path: str):
        """Replace the original image widget until the movie completes, and then change it back"""
        self.animation_widget = AnimationWidget(file_path)

        self.main_layout_wide.replaceWidget(self.image_widget, self.animation_widget)
        self.animation_widget.movie.finished.connect(self.replace_original_img_widget)
        self.animation_widget.run()

    @pyqtSlot()
    def replace_original_img_widget(self):
        self.main_layout_wide.replaceWidget(self.animation_widget, self.image_widget)

    def on_snap(self):
        self.snap_sound.play()
        self.reload_image()

    def on_full_snap(self):
        for i in reversed(range(1, 101)):
            self.gain_slider.setSliderPosition(i)
            self.reload_image()
            sleep(3 / i ** 2)
            # sleep(1)

    def reload_image(self):
        """
        Reload the image within the current frame, asking the underlying functions to recalculate
        based on its current values.
        """
        img = self.img_manager.update_image()

        q_image = PyQt5.QtGui.QImage.fromData(img.read())
        q_pixmap = PyQt5.QtGui.QPixmap.fromImage(q_image)

        self.image_widget.setPixmap(q_pixmap)

    def on_gain_slider_adjust(self):
        new_value = self.gain_slider.value()
        # TODO Scale this
        print(new_value)
        self.img_manager.gain = new_value

    def on_chunk_click(self):
        new_value = self.chunk_size_slider.value()
        self.img_manager.chunk_size = new_value

    def on_reset(self):
        self.img_manager.reset()


if __name__ == '__main__':
    app = QApplication([])

    g = GuiWindow(app, "kju.jpg")

    app.exit(app.exec_())
