import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

# iniciar app
app = QApplication([])

# cargar ui
login = uic.loadUi("window1.ui")
entrar = uic.loadUi("window2.ui")
error = uic.loadUi("window3.ui")

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(name) == 0 or len(password) == 0:
        login.label_5.setText("Error: Campos vacios")
    elif name == "admin" and password == "admin":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    entrar.show()
    login.hide()

def gui_error():
    login.hide()
    error.show()

def gui_regresar():
    login.show()
    error.hide()

def regresar_entrar():
    entrar.hide()
    login.label_5.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_5.setText("")
    login.show()

def salir():
    sys.exit()

#Botones

login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrar.pushButton.clicked.connect(regresar_entrar)
entrar.pushButton_2.clicked.connect(salir)

error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(salir)


# ejecutable
login.show()
app.exec()
