# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'photo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 453)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.photo = QLabel(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(0, 0, 531, 361))
        self.photo.setPixmap(QPixmap(u"image1.jpg"))
        self.photo.setScaledContents(True)
        self.Cat = QPushButton(self.centralwidget)
        self.Cat.setObjectName(u"Cat")
        self.Cat.setGeometry(QRect(20, 370, 191, 23))
        self.Dog = QPushButton(self.centralwidget)
        self.Dog.setObjectName(u"Dog")
        self.Dog.setGeometry(QRect(294, 370, 201, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 536, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.photo.setText("")
        self.Cat.setText(QCoreApplication.translate("MainWindow", u"Cat", None))
        self.Dog.setText(QCoreApplication.translate("MainWindow", u"Gog", None))
    # retranslateUi

