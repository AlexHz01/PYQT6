import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QBrush, QPixmap, QPalette
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('1.ui', self)

        self.btn_menu_uno.clicked.connect(self.mover_menu)
        self.btn_menu_dos.clicked.connect(self.mover_menu)

        #ocultar botones
        self.btn_restaurar.hide()
        self.btn_menu_dos.hide()

        #sombra de los widgets
        self.sombra_frame(self.stackedWidget)
        self.sombra_frame(self.frame_superior)
        self.sombra_frame(self.toolBox)
        self.sombra_frame(self.btn_uno)
        self.sombra_frame(self.btn_dos)
        self.sombra_frame(self.btn_tres)
        self.sombra_frame(self.btn_cuatro)

        #barra de titulos
        self.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.btn_restaurar.clicked.connect(self.control_btn_normal)
        self.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())

        #eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #size Grip

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #acceder paginas

        self.btn_uno.clicked.connect(self.pagina_uno)
        self.btn_dos.clicked.connect(self.pagina_dos)
        self.btn_tres.clicked.connect(self.pagina_tres)
        self.btn_cuatro.clicked.connect(self.pagina_cuatro)


    def control_btn_minimizar(self):
        self.showMinimized()

    def control_btn_normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()

    def sombra_frame(self, frame):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(8)
        shadow.setYOffset(8)
        shadow.setColor(QColor(20, 200, 220, 225))
        frame.setGraphicsEffect(shadow)

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalY() <= 10:
            self.showMaximized()
            self.btn_maximizar.hide()
            self.btn_restaurar.show()
        else:
            self.showNormal()
            self.btn_restaurar.hide()
            self.btn_maximizar.show()

    def mover_menu(self):
        if True:
            width = self.frame_2.width()
            normal = 0
            if width == 0:
                width_extend = 200
                width = width_extend
                self.btn_menu_dos.hide()
                self.btn_menu_uno.show()
            else:
                self.btn_menu_dos.show()
                self.btn_menu_uno.hide()
                width_extend = normal
            self.animation = QPropertyAnimation(self.frame_2, b"maximumWidth")
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extend)
            self.animation.setDuration(300)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def pagina_uno(self):
        self.stackedWidget.setCurrentWidget(self.page_uno)
        self.animacion_paginas()
    def pagina_dos(self):
        self.stackedWidget.setCurrentWidget(self.page_dos)
        self.animacion_paginas()
    def pagina_tres(self):
        self.stackedWidget.setCurrentWidget(self.page_tres)
        self.animacion_paginas()
    def pagina_cuatro(self):
        self.stackedWidget.setCurrentWidget(self.page_cuatro)
        self.animacion_paginas()

    def animacion_paginas(self):
        if True:
            width = self.stackedWidget.width()
            x1 = self.frame_pagina.rect().right()
            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = normal
            self.animation = QPropertyAnimation(self.stackedWidget, b"maximumWidth")
            self.animation.setStartValue(width)
            self.animation.setEndValue(extender)
            self.animation.setDuration(300)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())