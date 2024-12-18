# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# ================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

import os # Tarvitaan mm. hakemistopolkujen käsittelyyn
import sys # Tarvitaan sovelluksen argumenttien käsittelyyn
from PySide6 import QtCore, QtGui, QtWidgets # Tärekeimät Qt:n moduulit
from PySide6.QtUiTools import QUiLoader # Tarvitaan käyttöliittymätiedoston lataamiseen

# KÄYTTÖLIITTYMÄN LUOMINEN
# ------------------------

# Luodaan käyttöliittymätiedoston lataajaobjekti QUiLoader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perusteella, pääikkunalla ei ole isäntäobjektia
window = loader.load("mainWindow.ui", None)

# Asetetaan pääikkunan nimi
window.setWindowTitle('TÄMÄ ON PÄÄIKKUNA')

# Luodaan osoitin (pointer), joka viittaa käyttöliittymän elementtiin label
label = window.findChild(QtWidgets.QLabel, 'label')

statusBar = window.findChild(QtWidgets.QStatusBar, 'statusbar')
statusBar.showMessage('Kaikki hyvin', -1)

label != None
label.setText('Muutettu tekstiä')



# Määritellään ikkuna näkyväksi
window.show()

# Ajetaan sovellus
app.exec()