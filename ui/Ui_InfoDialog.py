# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageboxmUstYO.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName(u"InfoDialog")
        InfoDialog.setWindowModality(Qt.WindowModality.WindowModal)
        InfoDialog.resize(400, 180)
        InfoDialog.setStyleSheet(u"background-color:#2C2C2C;\n"
"color:white;\n"
"border-radius:8px;")
        InfoDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(InfoDialog)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label = QLabel(InfoDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(40, 25))
        self.label.setMaximumSize(QSize(44, 40))
        self.label.setPixmap(QPixmap(u"../app/icons/warn.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lbl_message = QLabel(InfoDialog)
        self.lbl_message.setObjectName(u"lbl_message")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_message.sizePolicy().hasHeightForWidth())
        self.lbl_message.setSizePolicy(sizePolicy1)
        self.lbl_message.setMinimumSize(QSize(0, 0))
        self.lbl_message.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.lbl_message.setFont(font)
        self.lbl_message.setScaledContents(False)
        self.lbl_message.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_message)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(110, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_OK = QPushButton(InfoDialog)
        self.btn_OK.setObjectName(u"btn_OK")
        self.btn_OK.setMaximumSize(QSize(120, 36))
        self.btn_OK.setCursor(QCursor(Qt.ArrowCursor))
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

        self.horizontalLayout_2.addWidget(self.btn_OK)

        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(InfoDialog)

        QMetaObject.connectSlotsByName(InfoDialog)
    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QCoreApplication.translate("InfoDialog", u"Dialog", None))
        self.label.setText("")
        self.lbl_message.setText(QCoreApplication.translate("InfoDialog", u"Information", None))
        self.btn_OK.setText(QCoreApplication.translate("InfoDialog", u"OK", None))
    # retranslateUi

