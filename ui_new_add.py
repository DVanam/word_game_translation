# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_add.ui_file'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(537, 478)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_textEd = QTextEdit(self.centralwidget)
        self.input_textEd.setObjectName(u"input_textEd")

        self.horizontalLayout.addWidget(self.input_textEd)

        self.output_textEd = QTextEdit(self.centralwidget)
        self.output_textEd.setObjectName(u"output_textEd")

        self.horizontalLayout.addWidget(self.output_textEd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"Add_btn")

        self.gridLayout.addWidget(self.add_btn, 0, 0, 1, 1)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"Delete_btn")

        self.gridLayout.addWidget(self.delete_btn, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

