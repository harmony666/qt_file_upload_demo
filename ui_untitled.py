# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)

# import SMB_Test
import send_choose


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(811, 632)
        self.choose = QPushButton(Dialog)
        self.choose.setObjectName(u"choose")
        self.choose.setGeometry(QRect(130, 160, 461, 31))
        self.send = QPushButton(Dialog)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(680, 200, 75, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 51, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 51, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 50, 51, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 110, 51, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 50, 51, 31))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 110, 81, 31))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 50, 51, 31))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 50, 69, 22))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 110, 69, 22))
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(300, 50, 69, 22))
        self.comboBox_4 = QComboBox(Dialog)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(300, 110, 69, 22))
        self.comboBox_5 = QComboBox(Dialog)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(460, 50, 69, 22))
        self.comboBox_6 = QComboBox(Dialog)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(650, 50, 69, 22))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(470, 110, 231, 21))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(90, 210, 79, 20))
        self.choose_2 = QPushButton(Dialog)
        self.choose_2.setObjectName(u"choose_2")
        self.choose_2.setGeometry(QRect(170, 200, 481, 31))
        self.comboBox_7 = QComboBox(Dialog)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(550, 270, 69, 22))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 270, 51, 31))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 270, 51, 31))
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(500, 270, 51, 31))
        self.comboBox_8 = QComboBox(Dialog)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(400, 270, 69, 22))
        self.comboBox_9 = QComboBox(Dialog)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(250, 270, 69, 22))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(360, 270, 51, 31))
        self.comboBox_10 = QComboBox(Dialog)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(110, 270, 69, 22))
        self.send_2 = QPushButton(Dialog)
        self.send_2.setObjectName(u"send_2")
        self.send_2.setGeometry(QRect(670, 270, 75, 24))
        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(100, 340, 591, 241))
        self.upsend = QLineEdit(Dialog)
        self.upsend.setObjectName(u"upsend")

        self.upsend.setGeometry(QRect(680, 160, 71, 21))
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(610, 160, 81, 31))

        self.retranslateUi(Dialog)
        # 绑定功能
        self.choose.clicked.connect(self.choose1)
        self.send.clicked.connect(self.send1)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.choose.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u5206\u6790\u62a5\u544a", None))
        self.send.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u4f20", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u9879\u76ee", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u9636\u6bb5", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u90e8\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u7c7b\u578b", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u8d23\u4efb\u5de5\u7a0b\u5e08", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5206\u6790\u7ed3\u679c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_5.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u5173\u8054\u6a21\u578b", None))
        self.choose_2.setText(QCoreApplication.translate("Dialog", u"\u5173\u8054\u591a\u4e2a\u6a21\u578b", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u9636\u6bb5\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u5e08\uff1a", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u7cfb\u7edf\uff1a", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))

        self.send_2.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5b58\u5165\u7f16\u53f7\uff1a", None))
    # retranslateUi

    def choose1(self):
        global f_path
        f_path = send_choose.choose()
    def send1(self):
        send_choose.send()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Ui = Ui_Dialog()   #Ui_Form()为类的名字，需要自行修改
    Ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())   #若不加此语句则程序运行不报错，但是窗口不弹出。
