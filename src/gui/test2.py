import PyQt5.QtWidgets
from time import sleep


app = PyQt5.QtWidgets.QApplication([])

window = PyQt5.QtWidgets.QWidget()

progress_bar = PyQt5.QtWidgets.QProgressBar()

progress_bar.show()

for i in range(1, 101):
    progress_bar.setValue(i)
    sleep(1 / i)


app.exec_()
