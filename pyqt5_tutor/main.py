"""Console script for pyqt5_tutor."""
import sys
import argparse
import logging
import logging.config
from PyQt5 import QtWidgets

from pyqt5_tutor.settings import LOGGER
from pyqt5_tutor.windows import MainWindow

logging.config.dictConfig(LOGGER)
logger = logging.getLogger(__name__)


def main():
    """Console script for pyqt5_tutor."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "pyqt5_tutor.cli.main")
    app = QtWidgets.QApplication(args._)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
