# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vaultfacefNhlDb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_VaultFace(object):
    def setupUi(self, VaultFace):
        if not VaultFace.objectName():
            VaultFace.setObjectName(u"VaultFace")
        VaultFace.resize(881, 710)
        VaultFace.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.centralwidget = QWidget(VaultFace)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color:#EEEEEE;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.panel_top = QWidget(self.centralwidget)
        self.panel_top.setObjectName(u"panel_top")
        self.panel_top.setMinimumSize(QSize(0, 80))
        self.panel_top.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(4)
        self.panel_top.setFont(font)
        self.panel_top.setStyleSheet(u"background-color:#2C2C2C;")
        self.horizontalLayout = QHBoxLayout(self.panel_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 8, 0)
        self.label = QLabel(self.panel_top)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 80))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:#2C2C2C;\n"
"color: #fcd33e;")
        self.label.setScaledContents(False)
        self.label.setMargin(15)
        self.label.setIndent(13)

        self.horizontalLayout.addWidget(self.label)

        self.btn_add_data = QPushButton(self.panel_top)
        self.btn_add_data.setObjectName(u"btn_add_data")
        self.btn_add_data.setMaximumSize(QSize(180, 16777215))
        self.btn_add_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_data.setTabletTracking(False)
        self.btn_add_data.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_add_data)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_add_vault = QPushButton(self.panel_top)
        self.btn_add_vault.setObjectName(u"btn_add_vault")
        self.btn_add_vault.setMaximumSize(QSize(180, 16777215))
        self.btn_add_vault.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_vault.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_add_vault)


        self.verticalLayout.addWidget(self.panel_top)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(False)
        self.panel_left = QWidget(self.splitter)
        self.panel_left.setObjectName(u"panel_left")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel_left.sizePolicy().hasHeightForWidth())
        self.panel_left.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.panel_left)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.panel_left)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setMinimumSize(QSize(250, 0))
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.treeWidget.setFont(font2)
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.treeWidget.setStyleSheet(u"background-color: #252526;")
        self.treeWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.treeWidget.setLineWidth(0)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.splitter.addWidget(self.panel_left)
        self.panel_right = QWidget(self.splitter)
        self.panel_right.setObjectName(u"panel_right")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.panel_right.sizePolicy().hasHeightForWidth())
        self.panel_right.setSizePolicy(sizePolicy2)
        self.panel_right.setStyleSheet(u"background-color: #1E1E1E;\n"
"font-size:16px;")
        self.verticalLayout_3 = QVBoxLayout(self.panel_right)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.panel_right)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.verticalLayout_4 = QVBoxLayout(self.page_data)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_data)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"margin-bottom:4px;")

        self.verticalLayout_4.addWidget(self.label_3)

        self.edit_parent = QLineEdit(self.page_data)
        self.edit_parent.setObjectName(u"edit_parent")
        self.edit_parent.setEnabled(False)
        self.edit_parent.setMinimumSize(QSize(0, 33))
        font3 = QFont()
        self.edit_parent.setFont(font3)
        self.edit_parent.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"height:38px;\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")

        self.verticalLayout_4.addWidget(self.edit_parent)

        self.label_2 = QLabel(self.page_data)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"margin-bottom:4px;")

        self.verticalLayout_4.addWidget(self.label_2)

        self.edit_name = QLineEdit(self.page_data)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setMinimumSize(QSize(0, 33))
        self.edit_name.setFont(font3)
        self.edit_name.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"height:38px;\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")

        self.verticalLayout_4.addWidget(self.edit_name)

        self.label_4 = QLabel(self.page_data)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setStyleSheet(u"margin-top:10px;\n"
"margin-bottom:4px;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.select_cyfer = QComboBox(self.page_data)
        self.select_cyfer.addItem("")
        self.select_cyfer.addItem("")
        self.select_cyfer.addItem("")
        self.select_cyfer.addItem("")
        self.select_cyfer.addItem("")
        self.select_cyfer.setObjectName(u"select_cyfer")
        self.select_cyfer.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"height:38px;\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")
        self.select_cyfer.setMinimumContentsLength(3)

        self.verticalLayout_4.addWidget(self.select_cyfer)

        self.label_5 = QLabel(self.page_data)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"margin-top:10px;\n"
"margin-bottom:4px;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.edit_value = QLineEdit(self.page_data)
        self.edit_value.setObjectName(u"edit_value")
        self.edit_value.setMinimumSize(QSize(0, 33))
        self.edit_value.setFont(font3)
        self.edit_value.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"height:38px;\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")

        self.verticalLayout_4.addWidget(self.edit_value)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.btn_modify = QPushButton(self.page_data)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setMinimumSize(QSize(160, 0))
        self.btn_modify.setMaximumSize(QSize(160, 16777215))
        self.btn_modify.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_modify.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_modify)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_delete = QPushButton(self.page_data)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(160, 0))
        self.btn_delete.setMaximumSize(QSize(160, 16777215))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_data)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.verticalLayout_5 = QVBoxLayout(self.page_folder)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_folder = QLabel(self.page_folder)
        self.lbl_folder.setObjectName(u"lbl_folder")
        self.lbl_folder.setStyleSheet(u"margin-bottom:4px;")

        self.verticalLayout_5.addWidget(self.lbl_folder)

        self.edit_folder = QLineEdit(self.page_folder)
        self.edit_folder.setObjectName(u"edit_folder")
        self.edit_folder.setMinimumSize(QSize(0, 33))
        self.edit_folder.setFont(font3)
        self.edit_folder.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"height:38px;\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")

        self.verticalLayout_5.addWidget(self.edit_folder)

        self.verticalSpacer_4 = QSpacerItem(44, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.btn_save_folder = QPushButton(self.page_folder)
        self.btn_save_folder.setObjectName(u"btn_save_folder")
        self.btn_save_folder.setMinimumSize(QSize(160, 0))
        self.btn_save_folder.setMaximumSize(QSize(160, 16777215))
        self.btn_save_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_folder.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_save_folder)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_delete_folder = QPushButton(self.page_folder)
        self.btn_delete_folder.setObjectName(u"btn_delete_folder")
        self.btn_delete_folder.setMinimumSize(QSize(160, 0))
        self.btn_delete_folder.setMaximumSize(QSize(160, 16777215))
        self.btn_delete_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_folder.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_delete_folder)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 451, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_folder)
        self.page_folders = QWidget()
        self.page_folders.setObjectName(u"page_folders")
        self.verticalLayout_6 = QVBoxLayout(self.page_folders)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.listView = QListView(self.page_folders)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"background-color: #333;\n"
"\n"
"color:white;\n"
"\n"
"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"padding: 0 8;")
        self.listView.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_6.addWidget(self.listView)

        self.stackedWidget.addWidget(self.page_folders)
        self.page_datas = QWidget()
        self.page_datas.setObjectName(u"page_datas")
        self.verticalLayout_7 = QVBoxLayout(self.page_datas)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableDatas = QTableWidget(self.page_datas)
        self.tableDatas.setObjectName(u"tableDatas")
        self.tableDatas.setStyleSheet(u"border-radius:5px;\n"
"border: 1px solid #AAA;\n"
"")

        self.verticalLayout_7.addWidget(self.tableDatas)

        self.stackedWidget.addWidget(self.page_datas)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.splitter.addWidget(self.panel_right)

        self.verticalLayout.addWidget(self.splitter)

        VaultFace.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VaultFace)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 33))
        VaultFace.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VaultFace)
        self.statusbar.setObjectName(u"statusbar")
        VaultFace.setStatusBar(self.statusbar)

        self.retranslateUi(VaultFace)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VaultFace)
    # setupUi

    def retranslateUi(self, VaultFace):
        VaultFace.setWindowTitle(QCoreApplication.translate("VaultFace", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("VaultFace", u"Vault Face", None))
        self.btn_add_data.setText(QCoreApplication.translate("VaultFace", u"Ajouter Donn\u00e9e", None))
        self.btn_add_vault.setText(QCoreApplication.translate("VaultFace", u"Ajouter Dossier", None))
        self.label_3.setText(QCoreApplication.translate("VaultFace", u"Dossier parent", None))
        self.label_2.setText(QCoreApplication.translate("VaultFace", u"Nom de la donn\u00e9e", None))
        self.label_4.setText(QCoreApplication.translate("VaultFace", u"Type de chiffrement", None))
        self.select_cyfer.setItemText(0, QCoreApplication.translate("VaultFace", u"AES", None))
        self.select_cyfer.setItemText(1, QCoreApplication.translate("VaultFace", u"RSA", None))
        self.select_cyfer.setItemText(2, QCoreApplication.translate("VaultFace", u"ChaCha20", None))
        self.select_cyfer.setItemText(3, QCoreApplication.translate("VaultFace", u"Blowfish", None))
        self.select_cyfer.setItemText(4, QCoreApplication.translate("VaultFace", u"DES ", None))

        self.label_5.setText(QCoreApplication.translate("VaultFace", u"Valeur", None))
        self.btn_modify.setText(QCoreApplication.translate("VaultFace", u"Valider", None))
        self.btn_delete.setText(QCoreApplication.translate("VaultFace", u"Supprimer", None))
        self.lbl_folder.setText(QCoreApplication.translate("VaultFace", u"Nom du dossier", None))
        self.btn_save_folder.setText(QCoreApplication.translate("VaultFace", u"Valider", None))
        self.btn_delete_folder.setText(QCoreApplication.translate("VaultFace", u"Supprimer", None))
    # retranslateUi

