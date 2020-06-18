"""
windows collection
"""
import logging
from PyQt5 import QtWidgets

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("MainWindow")
