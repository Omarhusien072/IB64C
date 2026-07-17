from PySide6 import QtWidgets as qtw, QtCore as qtc
from IB64C_UI.Logic.IB64C_Logic import IB64C_Logic
import sys


def main():
    app = qtw.QApplication(sys.argv)
    app.setEffectEnabled(qtc.Qt.UIEffect.UI_AnimateCombo, False)
    window = IB64C_Logic()
    window.ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
