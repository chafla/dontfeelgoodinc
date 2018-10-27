from PyQt5 import QtCore


class AnimationReadyEmitter(QtCore.QObject):

    # Create a trigger which has a single argument, denoting the filename of the ready argument.
    trigger = QtCore.pyqtSignal(str, name="animation_ready")

    def __init__(self):
        QtCore.QObject.__init__(self)

    def fire(self):
        self.trigger.emit()
