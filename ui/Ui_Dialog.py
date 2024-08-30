# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogXqrLuq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(400, 180)
        Dialog.setStyleSheet(u"background-color:#2C2C2C;\n"
"color:white;\n"
"border-radius:8px;")
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_message = QLabel(Dialog)
        self.lbl_message.setObjectName(u"lbl_message")
        font = QFont()
        font.setPointSize(12)
        self.lbl_message.setFont(font)
        self.lbl_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_message)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 36, -1, -1)
        self.btn_OK = QPushButton(Dialog)
        self.btn_OK.setObjectName(u"btn_OK")
        self.btn_OK.setStyleSheet(u"QPushButton{\n"
"	background-color: #4caf50;\n"
"	border-radius:8px;\n"
"	color:white;\n"
"	height:38px;\n"
"	font-size:16px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #4caf20;\n"
"	border-radius:8px;\n"
"	height:38px;\n"
"	font-size:16px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_OK)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: #f44336;\n"
"	border-radius:8px;\n"
"	color:white;\n"
"	height:38px;\n"
"	font-size:16px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #f14316;\n"
"	border-radius:8px;\n"
"	height:38px;\n"
"	font-size:16px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_message.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.btn_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

