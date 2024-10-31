# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUIawwgsS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import serial
import asyncio
import time
from PySide6.QtCore import *
from playsound import playsound
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import PySide6.QtWidgets
import cv2
import os
from datetime import datetime,timedelta
import io
from PIL import Image

import sqlite3
first_line=""
with open('port.txt') as f:
    first_line = f.readline().strip('\n')
arduino=""
try:
    arduino = serial.Serial(port=first_line,   baudrate=9600, timeout=.1)
except:
    pass
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 577)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabBarAutoHide(False)
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.gridLayout_3 = QGridLayout(self.Main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ClnImage = QLabel(self.Main)
        self.ClnImage.setObjectName(u"ClnImage")
        self.ClnImage.setMaximumSize(QSize(200, 200))
        self.ClnImage.setLayoutDirection(Qt.LeftToRight)
        self.ClnImage.setPixmap(QPixmap(u"res/profile.jpg"))
        self.ClnImage.setScaledContents(True)
        self.ClnImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.ClnImage)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.FName = QLabel(self.Main)
        self.FName.setObjectName(u"FName")
        self.FName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.FName)

        self.CSerial = QLabel(self.Main)
        self.CSerial.setObjectName(u"CSerial")

        self.verticalLayout_2.addWidget(self.CSerial)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SubDate = QLabel(self.Main)
        self.SubDate.setObjectName(u"SubDate")

        self.horizontalLayout_2.addWidget(self.SubDate)

        self.ExpDate = QLabel(self.Main)
        self.ExpDate.setObjectName(u"ExpDate")

        self.horizontalLayout_2.addWidget(self.ExpDate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Description = QLabel(self.Main)
        self.Description.setObjectName(u"Description")

        self.verticalLayout_2.addWidget(self.Description)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.CheckState = QLabel(self.Main)
        self.CheckState.setObjectName(u"CheckState")
        self.CheckState.setStyleSheet(u"background-color:lightgreen;color:black;")
        self.CheckState.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.CheckState)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Main, "")
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.verticalLayout_4 = QVBoxLayout(self.Tools)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.Tools)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -172, 889, 774))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ImgModCap = QLabel(self.scrollAreaWidgetContents)
        self.ImgModCap.setObjectName(u"ImgModCap")
        self.ImgModCap.setMaximumSize(QSize(200, 200))
        self.ImgModCap.setPixmap(QPixmap(u"res/profile.jpg"))
        self.ImgModCap.setScaledContents(True)
        self.ImgModCap.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.ImgModCap, 0, 0, 1, 1)

        self.ModCapBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ModCapBtn.setObjectName(u"ModCapBtn")

        self.gridLayout_5.addWidget(self.ModCapBtn, 1, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_16.addWidget(self.label_2)

        self.ModSearch = QLineEdit(self.scrollAreaWidgetContents)
        self.ModSearch.setObjectName(u"ModSearch")

        self.horizontalLayout_16.addWidget(self.ModSearch)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.ModFN = QLineEdit(self.scrollAreaWidgetContents)
        self.ModFN.setObjectName(u"ModFN")

        self.horizontalLayout_11.addWidget(self.ModFN)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.ModDE = QDateEdit(self.scrollAreaWidgetContents)
        self.ModDE.setObjectName(u"ModDE")

        self.horizontalLayout_14.addWidget(self.ModDE)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 2, 0, 2)
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.ModDesc = QTextEdit(self.scrollAreaWidgetContents)
        self.ModDesc.setObjectName(u"ModDesc")

        self.horizontalLayout_15.addWidget(self.ModDesc)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 2)

        self.horizontalLayout_10.addLayout(self.verticalLayout_10)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.ModBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ModBtn.setObjectName(u"ModBtn")

        self.verticalLayout_8.addWidget(self.ModBtn)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 3)
        self.verticalLayout_8.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_8, 3, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.DelCS = QLineEdit(self.scrollAreaWidgetContents)
        self.DelCS.setObjectName(u"DelCS")

        self.horizontalLayout_13.addWidget(self.DelCS)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.DelBtn = QPushButton(self.scrollAreaWidgetContents)
        self.DelBtn.setObjectName(u"DelBtn")

        self.verticalLayout_11.addWidget(self.DelBtn)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 3)
        self.verticalLayout_11.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_11, 4, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.ImgAddCap = QLabel(self.scrollAreaWidgetContents)
        self.ImgAddCap.setObjectName(u"ImgAddCap")
        self.ImgAddCap.setMaximumSize(QSize(200, 200))
        self.ImgAddCap.setPixmap(QPixmap(u"res/profile.jpg"))
        self.ImgAddCap.setScaledContents(True)
        self.ImgAddCap.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.ImgAddCap, 0, 0, 1, 1)

        self.AddCapBtn = QPushButton(self.scrollAreaWidgetContents)
        self.AddCapBtn.setObjectName(u"AddCapBtn")

        self.gridLayout_6.addWidget(self.AddCapBtn, 1, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.AddFN = QLineEdit(self.scrollAreaWidgetContents)
        self.AddFN.setObjectName(u"AddFN")

        self.horizontalLayout_4.addWidget(self.AddFN)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.AddCS = QLineEdit(self.scrollAreaWidgetContents)
        self.AddCS.setObjectName(u"AddCS")

        self.horizontalLayout_5.addWidget(self.AddCS)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.AddDE = QDateEdit(self.scrollAreaWidgetContents)
        self.AddDE.setObjectName(u"AddDE")

        self.horizontalLayout_6.addWidget(self.AddDE)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 2, -1, 2)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.AddDesc = QTextEdit(self.scrollAreaWidgetContents)
        self.AddDesc.setObjectName(u"AddDesc")

        self.horizontalLayout_7.addWidget(self.AddDesc)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.AddBtn = QPushButton(self.scrollAreaWidgetContents)
        self.AddBtn.setObjectName(u"AddBtn")

        self.verticalLayout_3.addWidget(self.AddBtn)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.Tools, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.SearchLine = QLineEdit(self.tab_3)
        self.SearchLine.setObjectName(u"SearchLine")

        self.horizontalLayout_8.addWidget(self.SearchLine)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.scrollArea_2 = QScrollArea(self.tab_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 892, 509))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.scrollArea_2)

        self.verticalLayout_12.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ClnImage.setText("")
        self.FName.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.CSerial.setText(QCoreApplication.translate("MainWindow", u"Code ##########", None))
        self.SubDate.setText(QCoreApplication.translate("MainWindow", u"Date Sub", None))
        self.ExpDate.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"Description Details", None))
        self.CheckState.setText(QCoreApplication.translate("MainWindow", u"Valide", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), QCoreApplication.translate("MainWindow", u"Principale", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Modifier/Renouveler", None))
        self.ImgModCap.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nom Complet", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        self.ModDE.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.ModBtn.setText(QCoreApplication.translate("MainWindow", u"Modifier/Renouveler", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        self.DelBtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.ImgAddCap.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nom Complet", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        self.AddDE.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.AddBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tools), QCoreApplication.translate("MainWindow", u"Outils", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Recherche ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom Complet", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date Sub", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"recherche avanc\u00e9e", None))
        #RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        
        self.rowsCnt=1000
        for p in range(self.rowsCnt) :
            self.tableWidget.insertRow(p)

        self.codeSerialMain=""
        self.aftermonth=add_months(datetime.today(),1).strftime('%m/%d/%Y')

        self.AddDE.setDate(QDate.fromString(self.aftermonth,"MM/dd/yyyy"))
        self.ModDE.setDate(QDate.fromString(self.aftermonth,"MM/dd/yyyy"))
        CreateMTable()
        self.ImgCurrCamFr=QPixmap(u"res/profile.jpg")
        self.stt=True
        self.sttMod=True
        self.worker1=Cam1()
        self.worker1.start()
        self.worker1.ImgUp.connect(self.ImgUpdtSlot)
        self.AddBtn.clicked.connect(self.AjouterBtn)
        self.DelBtn.clicked.connect(self.DeleteBtn)
        self.ModBtn.clicked.connect(self.ModifierBtn)
        self.SearchLine.textChanged.connect(self.srhTxtEv)
    def srhTxtEv(self):
        workerSrch=Srch1()
        workerSrch.srchtxt=self.SearchLine.text()
        workerSrch.obgtb=self.tableWidget
        workerSrch.main=self.Main
        #workerSrch.cnt=self.tableWidget.rowCount()

        #workerSrch.sig.connect(self.delrow)
        #workerSrch.thrd.connect(self.Add2Tb)

        workerSrch.run()
    """
    def delrow(self,val):
        self.tableWidget.removeRow(val)"""
    """def Add2Tb(self,val):
        rowPosition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        pic=QPixmap(u""+f"res/Imgs/{val[1]}.jpg")
        self.lb = QLabel(self.Main)
        self.lb.setPixmap(pic)
        self.lb.setScaledContents(True)
        self.tableWidget.setCellWidget(rowPosition,0, self.lb)
        self.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(val[0]))
        self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(val[1]))
        self.tableWidget.setItem(rowPosition , 3, QTableWidgetItem(val[2]))
        self.tableWidget.setItem(rowPosition , 4, QTableWidgetItem(val[3]))"""


    
    def ImgUpdtSlot(self,Image):
        if(self.stt):
            self.ImgAddCap.setPixmap(QPixmap.fromImage(Image))
        self.ImgCurrCamFr=QPixmap.fromImage(Image)
    def DeleteBtn(self):

        csvar=self.DelCS.text()
        self.DelCS.clear()
        details=self.AddDesc.toPlainText()
        if csvar!="" :
            exiterror=DelFM(csvar)
            if(exiterror=="success"):
                try:
                    os.remove(f"res/Imgs/{csvar}.jpg")
                except:
                    pass
                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Information) 

                # setting message for Message Box 
                msg_box_name.setText("done successfully") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Information") 
                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
            else:

                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Critical) 

                # setting message for Message Box 
                msg_box_name.setText(f"Error {exiterror}") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Error") 

                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
        else:

                msgWarning = QMessageBox() 

                msgWarning.setIcon(QMessageBox.Warning) 

                # setting message for Message Box 
                msgWarning.setText("Complete les entrees") 

                # setting Message box window title 
                msgWarning.setWindowTitle("Warning") 

                # declaring buttons on Message Box 
                msgWarning.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msgWarning.exec() 
    def AjouterBtn(self):
        fnvar=self.AddFN.text()
        csvar=self.AddCS.text()
        devar=self.AddDE.text()
        self.AddFN.clear()
        self.AddCS.clear()
        details=self.AddDesc.toPlainText()
        self.AddDesc.clear()
        if fnvar!="" and csvar!="" and devar!="" :
            dsvar=datetime.today().strftime('%m/%d/%Y')
            MyMember=Member(fnvar,csvar,dsvar,devar,details)
            exiterror=Add2M(MyMember)
            if(exiterror=="success"):
                pilmage=SaveIFQ2Pil(self.ImgAddCap)
                
                pilmage=pilmage.convert('RGB')
                pilmage.save(f"res/Imgs/{csvar}"+".jpg",quality=20,optimize=True)

                
                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Information) 

                # setting message for Message Box 
                msg_box_name.setText("done successfully") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Information") 
                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
            else:

                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Critical) 

                # setting message for Message Box 
                msg_box_name.setText(f"Error {exiterror}") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Error") 

                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
        else:

                msgWarning = QMessageBox() 

                msgWarning.setIcon(QMessageBox.Warning) 

                # setting message for Message Box 
                msgWarning.setText("Complete les entrees") 

                # setting Message box window title 
                msgWarning.setWindowTitle("Warning") 

                # declaring buttons on Message Box 
                msgWarning.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msgWarning.exec() 

                # retranslateUi
        
        self.AddDE.setDate(QDate.fromString(self.aftermonth,"MM/dd/yyyy"))
    
    def ModifierBtn(self):
        fnvar=self.ModFN.text()
        csvar=self.ModSearch.text()
        devar=self.ModDE.text()
        details=self.ModDesc.toPlainText()
        self.ModFN.clear()
        self.ModSearch.clear()
        self.ModDesc.clear()
        if fnvar!="" and csvar!="" and devar!="" :
            dsvar=datetime.today().strftime('%m/%d/%Y')
            MyMember=Member(fnvar,csvar,dsvar,devar,details)
            exiterror=ModFM(MyMember)
            if(exiterror=="success"):
                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Information) 

                # setting message for Message Box 
                msg_box_name.setText("done successfully") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Information") 
                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
            else:

                msg_box_name = QMessageBox() 

                msg_box_name.setIcon(QMessageBox.Critical) 

                # setting message for Message Box 
                msg_box_name.setText(f"Error {exiterror}") 

                # setting Message box window title 
                msg_box_name.setWindowTitle("Error") 

                # declaring buttons on Message Box 
                msg_box_name.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msg_box_name.exec() 
        else:

                msgWarning = QMessageBox() 

                msgWarning.setIcon(QMessageBox.Warning) 

                # setting message for Message Box 
                msgWarning.setText("Complete les entrees") 

                # setting Message box window title 
                msgWarning.setWindowTitle("Warning") 

                # declaring buttons on Message Box 
                msgWarning.setStandardButtons(QMessageBox.Ok ) 

                # start the app 
                msgWarning.exec() 

        
        self.ModDE.setDate(QDate.fromString(self.aftermonth,"MM/dd/yyyy"))
                # retranslateUi


def write_read():
    arduino.write(bytes('1','utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return   data
    
def SaveIFQ2Pil(Qmage):
    img=Qmage
    buffer=QBuffer()
    buffer.open(QBuffer.ReadWrite)
    img.pixmap().toImage().save(buffer,"JPG")
    PilImg=Image.open(io.BytesIO(buffer.data()))
    return PilImg

def CreateMTable():
    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query="""CREATE TABLE Members(
    FullName VARCHAR(300),
    CodeSerial VARCHAR(11) NOT NULL UNIQUE,
    DateSub VARCHAR(11),
    DateExp VARCHAR(11),
    Details VARCHAR(3000)
    )"""
    try:
        cursor.execute(query)
    except:
        pass
    finally:
        sqliteConnection.close()
def ModFM(Memb):

    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f"""UPDATE Members SET 
    FullName='{Memb.fname}',
    DateSub='{Memb.datesub}',
    DateExp='{Memb.dateexp}',
    Details='{Memb.more}'
    WHERE CodeSerial='{Memb.cserial}'
    """
    try:
        cursor.execute(query)
        sqliteConnection.commit()
    except:
        return "error"
    finally:
        sqliteConnection.close()
    return "success"
def GetAllM(Key):

    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f""" SELECT * FROM Members WHERE 
    FullName LIKE '%{Key}%' OR
    DateSub LIKE '%{Key}' OR
    DateExp LIKE '%{Key}' OR
    Details LIKE '%{Key}' OR
    CodeSerial LIKE '%{Key}%' COLLATE NOCASE"""
    data=""
    try:
        cursor.execute(query)
        data=cursor.fetchmany(200)
    except:
        return "error"
    finally:
        sqliteConnection.close()
        return data
def GetAllMExactByName(Key):

    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f""" SELECT * FROM Members WHERE 
    FullName='{Key}' COLLATE NOCASE """
    data=""
    try:
        cursor.execute(query)
        data=cursor.fetchmany(1000)
    except:
        return "error"
    finally:
        sqliteConnection.close()
        return data
def GetOneM(Code):

    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f"SELECT * FROM Members WHERE CodeSerial='{Code}'"
    data=""
    try:
        cursor.execute(query)
        data=cursor.fetchone()
    except:
        return "error"
    finally:
        sqliteConnection.close()
        return data
def DelFM(Code):

    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f"DELETE FROM Members WHERE CodeSerial='{Code}'"
    try:
        cursor.execute(query)
        sqliteConnection.commit()
    except:
        return "error"
    finally:
        sqliteConnection.close()
    return "success"
 
def add_months(current_date, months_to_add):
    if(current_date.day!=31):
    
        new_date = datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                        (current_date.month + months_to_add - 1) % 12 + 1,
                        current_date.day, current_date.hour, current_date.minute, current_date.second)
        return new_date
    else:
        new_date = datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                        (current_date.month + months_to_add ) % 12 + 1,
                        1, current_date.hour, current_date.minute, current_date.second)
        return new_date
def Add2M(Memb):
    sqliteConnection = sqlite3.connect('gym.db')
    cursor = sqliteConnection.cursor()
    query=f"""INSERT INTO Members(FullName,CodeSerial,DateSub,DateExp,Details)
    VALUES('{Memb.fname}','{Memb.cserial}','{Memb.datesub}','{Memb.dateexp}','{Memb.more}')
    """
    try:
        cursor.execute(query)
        sqliteConnection.commit()
    except:
        return "error"
    finally:
        sqliteConnection.close()
    return "success"
    
class Member:
    def __init__(self,Fname,CSerial,DateSub,DateExp,More):
        self.fname=Fname
        self.cserial=CSerial
        self.datesub=DateSub
        self.dateexp=DateExp
        self.more=More

class Cam1(QThread):
    ImgUp=Signal(QImage)
    Cap=cv2.VideoCapture(0)
    def run(self):
        self.ThreadActive=True
        while self.ThreadActive:
            if self.ThreadActive :
                ret,frame=self.Cap.read()
                if ret:
                    Image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    FlippedImg=cv2.flip(Image,1)
                    Cnv2Qt=QImage(FlippedImg.data,FlippedImg.shape[1],FlippedImg.shape[0],QImage.Format_RGB888)
                    pic=Cnv2Qt.scaled(640,480,Qt.KeepAspectRatio)
                    self.ImgUp.emit(pic)
    def stop(self):
        self.ThreadActive=False
        self.quit()

class Srch1(QThread):
    #thrd=Signal(tuple)
    #sig=Signal(int)
    obgtb=object
    main=object
    srchtxt=""
    def run(self):
        data=GetAllM(self.srchtxt)
        self.obgtb.clear()
        """
        ___qtablewidgetitem = self.obgtb.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        ___qtablewidgetitem1 = self.obgtb.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom Complet", None))
        ___qtablewidgetitem2 = self.obgtb.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        ___qtablewidgetitem3 = self.obgtb.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date Sub", None))
        ___qtablewidgetitem4 = self.obgtb.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        ___qtablewidgetitem5 = self.obgtb.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None))"""
        j=0
        for i in data:
            #self.thrd.emit(i)
            pic=QPixmap(u""+f"res/Imgs/{i[1]}.jpg")
            self.lb = QLabel(self.main)
            self.lb.setPixmap(pic)
            self.lb.setScaledContents(True)
            self.obgtb.setCellWidget(j,0, self.lb)
            self.obgtb.setItem(j , 1, QTableWidgetItem(i[0]))
            self.obgtb.setItem(j , 2, QTableWidgetItem(i[1]))
            self.obgtb.setItem(j , 3, QTableWidgetItem(i[2]))
            self.obgtb.setItem(j , 4, QTableWidgetItem(i[3]))
            j+=1
class Srch2(QThread):
    #thrd=Signal(tuple)
    #sig=Signal(int)
    obgtb=object
    main=object
    srchtxt=""
    def run(self):
        data=GetAllMExactByName(self.srchtxt)
        self.obgtb.clear()
        """
        ___qtablewidgetitem = self.obgtb.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        ___qtablewidgetitem1 = self.obgtb.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom Complet", None))
        ___qtablewidgetitem2 = self.obgtb.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Code Client", None))
        ___qtablewidgetitem3 = self.obgtb.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date Sub", None))
        ___qtablewidgetitem4 = self.obgtb.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date Exp", None))
        ___qtablewidgetitem5 = self.obgtb.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None))"""
        j=0
        for i in data:
            #self.thrd.emit(i)
            pic=QPixmap(u""+f"res/Imgs/{i[1]}.jpg")
            self.lb = QLabel(self.main)
            self.lb.setPixmap(pic)
            self.lb.setScaledContents(True)
            self.obgtb.setCellWidget(j,0, self.lb)
            self.obgtb.setItem(j , 1, QTableWidgetItem(i[0]))
            self.obgtb.setItem(j , 2, QTableWidgetItem(i[1]))
            self.obgtb.setItem(j , 3, QTableWidgetItem(i[2]))
            self.obgtb.setItem(j , 4, QTableWidgetItem(i[3]))
            j+=1



            

class MainWin(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        PySide6.QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        

    def keyPressEvent(self,event):
        varcont=self.ui
        booleanstate=(
        varcont.DelCS.hasFocus() or
        varcont.ModFN.hasFocus() or
        varcont.ModDE.hasFocus() or
        varcont.ModDesc.hasFocus() or
        varcont.AddFN.hasFocus() or
        varcont.AddCS.hasFocus() or
        varcont.AddDE.hasFocus() or
        varcont.AddDesc.hasFocus() )
        if(varcont.tabWidget.currentIndex()==0):
            varcont.CSerial.setText(varcont.codeSerialMain)
            if(event.key()==16777220):
                data=GetOneM(self.ui.codeSerialMain)
                if(data!=None):
                    try:
                        varcont.FName.setText(data[0])
                        varcont.SubDate.setText(data[2])
                        varcont.ExpDate.setText(data[3])
                        varcont.Description.setText(data[4])
                        try:
                            varcont.ClnImage.setPixmap(QPixmap(u"res/Imgs/"+varcont.codeSerialMain+".jpg"))
                        except:
                            varcont.ClnImage.setPixmap(QPixmap(u"res/profile.jpg"))

                    except:
                        varcont.FName.setText("null")
                        varcont.SubDate.setText("null")
                        varcont.ExpDate.setText("null")
                        varcont.Description.setText("null")
                    dateexp=datetime.strptime(data[3], "%m/%d/%Y")
                    delta=datetime.today()<=dateexp
                    if(delta):
                        varcont.CheckState.setText("valide")
                        varcont.CheckState.setStyleSheet(u"background-color:lightgreen;color:black;")
                        try:
                            write_read()
                        except:
                            pass
                    else:
                        varcont.CheckState.setText("Non valide")
                        varcont.CheckState.setStyleSheet(u"background-color:red;")
                        try:
                            playsound('res/Cancel.mp3')
                        except:
                            pass
                else:

                    varcont.FName.setText("N'existe pas")
                    varcont.Description.setText("N'existe pas")
                    varcont.ClnImage.setPixmap(QPixmap(u"res/profile.jpg"))
                    varcont.CheckState.setText("Non valide")
                    varcont.CheckState.setStyleSheet(u"background-color:red;")
                    try:
                        playsound('res/Cancel.mp3')
                    except:
                        pass

                varcont.codeSerialMain=""
            elif (event.key()>0 and event.key()<=255):
                varcont.codeSerialMain+=chr(event.key())
        elif(varcont.tabWidget.currentIndex()==1):
            if(event.key()==16777220 and varcont.ModSearch.text!="" and not booleanstate):
                data=GetOneM(varcont.ModSearch.text())
                if(data!=None):
                    varcont.ModFN.setText(data[0])
                    varcont.ModDesc.setText(data[4])
                    varcont.sttMod=not varcont.sttMod
                    try:
                        varcont.ImgModCap.setPixmap(QPixmap(u"res/Imgs/"+varcont.ModSearch.text()+".jpg"))
                    except:
                        varcont.ImgModCap.setPixmap(QPixmap(u"res/profile.jpg"))


            elif (event.key()>0 and event.key()<=255):
                varcont.ModSearch.setText(varcont.ModSearch.text()+chr(event.key()))
        elif(varcont.tabWidget.currentIndex()==2 and varcont.SearchLine.hasFocus()):
            if(event.key()==16777220 and varcont.SearchLine.text!=""):

                workerSrch2=Srch2()
                workerSrch2.srchtxt=varcont.SearchLine.text()
                workerSrch2.obgtb=varcont.tableWidget
                workerSrch2.main=varcont.Main
                #workerSrch.cnt=self.tableWidget.rowCount()
        
                #workerSrch.sig.connect(self.delrow)
                #workerSrch.thrd.connect(self.Add2Tb)
        
                workerSrch2.run()
                


    # retranslateUi
strcrypt=""
crypt={
    "0A":"a",
    "0B":"b",
    "0C":"c",
    "0D":"d",
    "0E":"e",
    "0F":"f",
    "A0":"g",
    "A1":"h",
    "A2":"i",
    "A3":"j",
    "A4":"k",
    "A5":"l",
    "A6":"m",
    "A7":"n",
    "A8":"o",
    "A9":"p",
    "AA":"q",
    "AB":"r",
    "AC":"s",
    "AD":"t",
    "AE":"u",
    "AF":"v",
    "B0":"w",
    "B1":"x",
    "B2":"y",
    "B3":"z",
    "B4":"A",
    "B5":"B",
    "B6":"C",
    "B7":"D",
    "B8":"E",
    "B9":"F",
    "BA":"G",
    "BB":"H",
    "BC":"I",
    "BD":"J",
    "BE":"K",
    "BF":"L",
    "C0":"M",
    "C1":"N",
    "C2":"O",
    "C3":"P",
    "C4":"Q",
    "C5":"R",
    "C6":"S",
    "C7":"T",
    "C8":"U",
    "C9":"V",
    "CA":"W",
    "CB":"X",
    "CC":"Y",
    "CD":"Z",
}
def ErrorLicense(winobj):
    msg_box_name = QMessageBox() 
    msg_box_name.setIcon(QMessageBox.Critical) 
    # setting message for Message Box 
    msg_box_name.setText("Error Application not activated contact seller for more details") 
    # setting Message box window title 
    msg_box_name.setWindowTitle("Access denied") 
    # declaring buttons on Message Box 
    msg_box_name.setStandardButtons(QMessageBox.Ok ) 
    # start the app 
    msg_box_name.exec() 
    winobj.close()
def decryt(strphenc):
    strph=""
    i=0
    while(i<len(strphenc)):
        if(strphenc[i:i+2] in crypt):
            strph+=crypt[strphenc[i:i+2]]
            i+=2
        else:
            strph+=strphenc[i]
            i+=1
    return strph

if __name__=="__main__":
    app=PySide6.QtWidgets.QApplication([])
    window=MainWin()
    window.show()
    try:
        with open('lic.txt') as f:
            strcrypt = f.readline().strip('\n')
            hfilepth=decryt(strcrypt)
            try:
                isAllowed=""
                with open(hfilepth) as file:
                    isAllowed = file.readline().strip('\n')
                if(isAllowed=="true"):
                    app.exec()

                else:

                    ErrorLicense(window)
            except:
                ErrorLicense(window)
    except:
        ErrorLicense(window)
    

