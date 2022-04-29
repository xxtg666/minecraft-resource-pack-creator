# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mrpcg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.s1_l = QLineEdit(self.groupBox)
        self.s1_l.setObjectName(u"s1_l")
        self.s1_l.setEnabled(True)

        self.horizontalLayout.addWidget(self.s1_l)

        self.s1_p = QPushButton(self.groupBox)
        self.s1_p.setObjectName(u"s1_p")

        self.horizontalLayout.addWidget(self.s1_p)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.s1_d = QPushButton(self.groupBox)
        self.s1_d.setObjectName(u"s1_d")

        self.verticalLayout.addWidget(self.s1_d)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.s2_l = QLineEdit(self.groupBox_2)
        self.s2_l.setObjectName(u"s2_l")
        self.s2_l.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.s2_l)

        self.s2_p = QPushButton(self.groupBox_2)
        self.s2_p.setObjectName(u"s2_p")

        self.horizontalLayout_2.addWidget(self.s2_p)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.step = QLabel(self.centralwidget)
        self.step.setObjectName(u"step")

        self.horizontalLayout_3.addWidget(self.step)

        self.nextstep = QPushButton(self.centralwidget)
        self.nextstep.setObjectName(u"nextstep")

        self.horizontalLayout_3.addWidget(self.nextstep)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MC\u4e00\u952e\u66ff\u6362\u6240\u6709\u6750\u8d28\u751f\u6210\u5668", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                                                                                 By xxtg666", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e0b\u8f7d\u597d\u7684packzip-mc-resource-pack-creator.zip\u6587\u4ef6", None))
        self.s1_p.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.s1_d.setText(QCoreApplication.translate("MainWindow", u"\u6ca1\u6709\uff1f\u70b9\u6b64\u4e0b\u8f7d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f60\u8981\u66ff\u6362\u7684\u56fe\u7247\u6587\u4ef6 .png\u683c\u5f0f\uff08\u628a\u6240\u6709\u6750\u8d28\u90fd\u53d8\u6210\u90a3\u4e00\u5f20\u56fe\uff09", None))
        self.s2_p.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5236\u4f5c\uff01", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8fdb\u5ea6\uff1a", None))
        self.step.setText(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.nextstep.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
    # retranslateUi

