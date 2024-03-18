# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_game.ui_file'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(548, 463)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_text = QTextEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")

        self.verticalLayout_2.addWidget(self.input_text)

        self.output_text = QTextEdit(self.centralwidget)
        self.output_text.setObjectName(u"output_text")

        self.verticalLayout_2.addWidget(self.output_text)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 3)

        self.check_qeust_ans_text = QTextEdit(self.centralwidget)
        self.check_qeust_ans_text.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.check_qeust_ans_text, 0, 3, 2, 1)

        self.start_session = QPushButton(self.centralwidget)
        self.start_session.setObjectName(u"session_start")

        self.gridLayout.addWidget(self.start_session, 1, 0, 1, 1)

        self.save_word_button = QPushButton(self.centralwidget)
        self.save_word_button.setObjectName(u"add_save_text")

        self.gridLayout.addWidget(self.save_word_button, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ru_qeustion = QLabel(self.centralwidget)
        self.ru_qeustion.setObjectName(u"ru_text")

        self.gridLayout_2.addWidget(self.ru_qeustion, 2, 0, 1, 1)

        self.en_le_text = QLineEdit(self.centralwidget)
        self.en_le_text.setObjectName(u"en_text")

        self.gridLayout_2.addWidget(self.en_le_text, 3, 0, 1, 1)

        self.session_spinbox = QSpinBox(self.centralwidget)
        self.session_spinbox.setObjectName(u"session_spinbox")
        self.session_spinbox.setMinimum(1)

        self.gridLayout_2.addWidget(self.session_spinbox, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_session.setText(QCoreApplication.translate("MainWindow", u"Sesion", None))
        self.save_word_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ru_qeustion.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

