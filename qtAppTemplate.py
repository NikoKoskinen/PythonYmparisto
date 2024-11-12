# MALLIPOHJA QT-SOVELLUSTEN RAKENTAMISEEN
#========================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Järjestelmäkomentojen kirjasto
import sys

# QT:n kirjastot
#from PyQt6.QtWidgets import * # käyttöliittymän elementit (kaikki), korvaa listalla
#from PyQt6.uic import load_ui

# pyside-kirjastot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# LUOKKA MÄÄRITYKSET
# ------------------

# Pääikkunan luokka, joka perii QmainWindow- luokan
class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

    windowLoader = QUiLoader()

    uiFile = QFile('mainWindow.ui')
    window = windowLoader.load(uiFile)
    window.show()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())