"""Console script for pyqt5_tutor."""
import argparse
import sys
from PyQt5 import QtWidgets

from pyqt5_tutor.windows import MainWindow


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
