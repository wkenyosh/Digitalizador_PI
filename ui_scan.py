# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiscan.ui'
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
        MainWindow.resize(846, 685)
        self.Paginas = QWidget(MainWindow)
        self.Paginas.setObjectName(u"Paginas")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Paginas.sizePolicy().hasHeightForWidth())
        self.Paginas.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.Paginas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.Paginas)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_cvendas = QPushButton(self.frame)
        self.btn_cvendas.setObjectName(u"btn_cvendas")

        self.horizontalLayout.addWidget(self.btn_cvendas)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.Paginas)
        self.Pages.setObjectName(u"Pages")
        font = QFont()
        font.setPointSize(11)
        self.Pages.setFont(font)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_2 = QVBoxLayout(self.home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(194, 194, 194);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.widget)

        self.Pages.addWidget(self.home)
        self.Cad_vendas = QWidget()
        self.Cad_vendas.setObjectName(u"Cad_vendas")
        self.horizontalLayout_16 = QHBoxLayout(self.Cad_vendas)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.Cad_vendas)
        self.label_26.setObjectName(u"label_26")
        font1 = QFont()
        font1.setPointSize(30)
        self.label_26.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_26)

        self.label_25 = QLabel(self.Cad_vendas)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_25)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(self.Cad_vendas)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_17)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.Cad_vendas)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.Cad_vendas)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(130, 35))
        self.label_13.setMaximumSize(QSize(130, 35))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_13.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.entry_numerocoo = QLineEdit(self.Cad_vendas)
        self.entry_numerocoo.setObjectName(u"entry_numerocoo")
        self.entry_numerocoo.setMinimumSize(QSize(145, 25))
        self.entry_numerocoo.setMaximumSize(QSize(145, 25))
        self.entry_numerocoo.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.entry_numerocoo)

        self.label_5 = QLabel(self.Cad_vendas)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.Cad_vendas)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.label_14 = QLabel(self.Cad_vendas)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(130, 35))
        self.label_14.setMaximumSize(QSize(130, 35))
        self.label_14.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.entry_datavenda = QLineEdit(self.Cad_vendas)
        self.entry_datavenda.setObjectName(u"entry_datavenda")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entry_datavenda.sizePolicy().hasHeightForWidth())
        self.entry_datavenda.setSizePolicy(sizePolicy1)
        self.entry_datavenda.setMinimumSize(QSize(145, 25))
        self.entry_datavenda.setMaximumSize(QSize(145, 25))

        self.horizontalLayout_12.addWidget(self.entry_datavenda)

        self.label_6 = QLabel(self.Cad_vendas)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.Cad_vendas)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.label_15 = QLabel(self.Cad_vendas)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(130, 35))
        self.label_15.setMaximumSize(QSize(130, 35))
        self.label_15.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.entry_cpf = QLineEdit(self.Cad_vendas)
        self.entry_cpf.setObjectName(u"entry_cpf")
        self.entry_cpf.setMinimumSize(QSize(145, 25))
        self.entry_cpf.setMaximumSize(QSize(145, 25))

        self.horizontalLayout_13.addWidget(self.entry_cpf)

        self.label_7 = QLabel(self.Cad_vendas)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_13.addWidget(self.label_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.Cad_vendas)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_14.addWidget(self.label_24)

        self.label_16 = QLabel(self.Cad_vendas)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(130, 35))
        self.label_16.setMaximumSize(QSize(130, 35))
        self.label_16.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_16)

        self.entry_automs = QLineEdit(self.Cad_vendas)
        self.entry_automs.setObjectName(u"entry_automs")
        self.entry_automs.setMinimumSize(QSize(145, 25))
        self.entry_automs.setMaximumSize(QSize(145, 25))

        self.horizontalLayout_14.addWidget(self.entry_automs)

        self.label_8 = QLabel(self.Cad_vendas)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.Cad_vendas)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.btn_consultas = QPushButton(self.Cad_vendas)
        self.btn_consultas.setObjectName(u"btn_consultas")
        self.btn_consultas.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_consultas.setFont(font4)

        self.horizontalLayout_15.addWidget(self.btn_consultas)

        self.label_27 = QLabel(self.Cad_vendas)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setMinimumSize(QSize(50, 35))
        self.label_27.setMaximumSize(QSize(50, 35))

        self.horizontalLayout_15.addWidget(self.label_27)

        self.btn_enviarcad = QPushButton(self.Cad_vendas)
        self.btn_enviarcad.setObjectName(u"btn_enviarcad")
        sizePolicy1.setHeightForWidth(self.btn_enviarcad.sizePolicy().hasHeightForWidth())
        self.btn_enviarcad.setSizePolicy(sizePolicy1)
        self.btn_enviarcad.setMinimumSize(QSize(0, 35))
        self.btn_enviarcad.setMaximumSize(QSize(75, 35))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_enviarcad.setFont(font5)

        self.horizontalLayout_15.addWidget(self.btn_enviarcad)

        self.label_9 = QLabel(self.Cad_vendas)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(50, 35))
        self.label_9.setMaximumSize(QSize(50, 35))

        self.horizontalLayout_15.addWidget(self.label_9)

        self.btn_EscanearDoc = QPushButton(self.Cad_vendas)
        self.btn_EscanearDoc.setObjectName(u"btn_EscanearDoc")
        sizePolicy1.setHeightForWidth(self.btn_EscanearDoc.sizePolicy().hasHeightForWidth())
        self.btn_EscanearDoc.setSizePolicy(sizePolicy1)
        self.btn_EscanearDoc.setMinimumSize(QSize(175, 35))
        self.btn_EscanearDoc.setMaximumSize(QSize(175, 35))
        self.btn_EscanearDoc.setFont(font5)

        self.horizontalLayout_15.addWidget(self.btn_EscanearDoc)

        self.label_10 = QLabel(self.Cad_vendas)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_16.addLayout(self.verticalLayout_6)

        self.Pages.addWidget(self.Cad_vendas)
        self.EscanearDoc = QWidget()
        self.EscanearDoc.setObjectName(u"EscanearDoc")
        self.verticalLayout_3 = QVBoxLayout(self.EscanearDoc)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.EscanearDoc)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_12 = QVBoxLayout(self.tab1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 36))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_scan1 = QLabel(self.scrollAreaWidgetContents)
        self.label_scan1.setObjectName(u"label_scan1")
        self.label_scan1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_scan1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.frame_13 = QFrame(self.tab1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_ocrTab1 = QPushButton(self.frame_13)
        self.btn_ocrTab1.setObjectName(u"btn_ocrTab1")
        self.btn_ocrTab1.setMinimumSize(QSize(146, 0))

        self.horizontalLayout_33.addWidget(self.btn_ocrTab1)

        self.horizontalSpacer_9 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_9)

        self.btn_salvar1 = QPushButton(self.frame_13)
        self.btn_salvar1.setObjectName(u"btn_salvar1")

        self.horizontalLayout_33.addWidget(self.btn_salvar1)

        self.btn_digitalizarTab1 = QPushButton(self.frame_13)
        self.btn_digitalizarTab1.setObjectName(u"btn_digitalizarTab1")

        self.horizontalLayout_33.addWidget(self.btn_digitalizarTab1)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_14 = QVBoxLayout(self.tab2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 36))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_scan2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_scan2.setObjectName(u"label_scan2")
        self.label_scan2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_scan2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea_2)

        self.frame_11 = QFrame(self.tab2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_ocrTab2 = QPushButton(self.frame_11)
        self.btn_ocrTab2.setObjectName(u"btn_ocrTab2")

        self.horizontalLayout_29.addWidget(self.btn_ocrTab2)

        self.horizontalSpacer_7 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_7)

        self.btn_salvar2 = QPushButton(self.frame_11)
        self.btn_salvar2.setObjectName(u"btn_salvar2")

        self.horizontalLayout_29.addWidget(self.btn_salvar2)

        self.btn_digitalizarTab2 = QPushButton(self.frame_11)
        self.btn_digitalizarTab2.setObjectName(u"btn_digitalizarTab2")

        self.horizontalLayout_29.addWidget(self.btn_digitalizarTab2)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_29)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_10 = QVBoxLayout(self.tab3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_3 = QScrollArea(self.tab3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 98, 36))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_scan3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_scan3.setObjectName(u"label_scan3")
        self.label_scan3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_scan3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.frame_9 = QFrame(self.tab3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_ocrTab3 = QPushButton(self.frame_9)
        self.btn_ocrTab3.setObjectName(u"btn_ocrTab3")

        self.horizontalLayout_27.addWidget(self.btn_ocrTab3)

        self.horizontalSpacer_6 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_6)

        self.btn_salvar3 = QPushButton(self.frame_9)
        self.btn_salvar3.setObjectName(u"btn_salvar3")

        self.horizontalLayout_27.addWidget(self.btn_salvar3)

        self.btn_digitalizarTab3 = QPushButton(self.frame_9)
        self.btn_digitalizarTab3.setObjectName(u"btn_digitalizarTab3")

        self.horizontalLayout_27.addWidget(self.btn_digitalizarTab3)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.verticalLayout_9 = QVBoxLayout(self.tab4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_4 = QScrollArea(self.tab4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 98, 36))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_scan4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_scan4.setObjectName(u"label_scan4")
        self.label_scan4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_scan4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_9.addWidget(self.scrollArea_4)

        self.frame_7 = QFrame(self.tab4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.btn_ocrTab4 = QPushButton(self.frame_7)
        self.btn_ocrTab4.setObjectName(u"btn_ocrTab4")
        self.btn_ocrTab4.setMinimumSize(QSize(146, 0))

        self.horizontalLayout_25.addWidget(self.btn_ocrTab4)

        self.horizontalSpacer_5 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_5)

        self.btn_salvar4 = QPushButton(self.frame_7)
        self.btn_salvar4.setObjectName(u"btn_salvar4")

        self.horizontalLayout_25.addWidget(self.btn_salvar4)

        self.btn_digitalizarTab4 = QPushButton(self.frame_7)
        self.btn_digitalizarTab4.setObjectName(u"btn_digitalizarTab4")

        self.horizontalLayout_25.addWidget(self.btn_digitalizarTab4)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.verticalLayout_15 = QVBoxLayout(self.tab5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_5 = QScrollArea(self.tab5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 98, 36))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_scan5 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_scan5.setObjectName(u"label_scan5")
        self.label_scan5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_scan5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_15.addWidget(self.scrollArea_5)

        self.frame_5 = QFrame(self.tab5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_ocrTab5 = QPushButton(self.frame_5)
        self.btn_ocrTab5.setObjectName(u"btn_ocrTab5")

        self.horizontalLayout_22.addWidget(self.btn_ocrTab5)

        self.horizontalSpacer_4 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_4)

        self.btn_salvar5 = QPushButton(self.frame_5)
        self.btn_salvar5.setObjectName(u"btn_salvar5")

        self.horizontalLayout_22.addWidget(self.btn_salvar5)

        self.btn_digitalizarTab5 = QPushButton(self.frame_5)
        self.btn_digitalizarTab5.setObjectName(u"btn_digitalizarTab5")

        self.horizontalLayout_22.addWidget(self.btn_digitalizarTab5)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab5, "")
        self.tab6 = QWidget()
        self.tab6.setObjectName(u"tab6")
        self.verticalLayout_7 = QVBoxLayout(self.tab6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_6 = QScrollArea(self.tab6)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 784, 421))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_scan6 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_scan6.setObjectName(u"label_scan6")
        self.label_scan6.setScaledContents(False)
        self.label_scan6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_scan6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_7.addWidget(self.scrollArea_6)

        self.frame_3 = QFrame(self.tab6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_ocrTab6 = QPushButton(self.frame_3)
        self.btn_ocrTab6.setObjectName(u"btn_ocrTab6")

        self.horizontalLayout_17.addWidget(self.btn_ocrTab6)

        self.horizontalSpacer_2 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)

        self.btn_salvar6 = QPushButton(self.frame_3)
        self.btn_salvar6.setObjectName(u"btn_salvar6")

        self.horizontalLayout_17.addWidget(self.btn_salvar6)

        self.btn_digitalizarTab6 = QPushButton(self.frame_3)
        self.btn_digitalizarTab6.setObjectName(u"btn_digitalizarTab6")

        self.horizontalLayout_17.addWidget(self.btn_digitalizarTab6)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab6, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.Pages.addWidget(self.EscanearDoc)
        self.tela_cadastro = QWidget()
        self.tela_cadastro.setObjectName(u"tela_cadastro")
        self.horizontalLayout_10 = QHBoxLayout(self.tela_cadastro)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.tela_cadastro)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_10.addWidget(self.label_22)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_telacadastro = QLabel(self.tela_cadastro)
        self.txt_telacadastro.setObjectName(u"txt_telacadastro")
        self.txt_telacadastro.setMaximumSize(QSize(16777215, 200))
        font6 = QFont()
        font6.setPointSize(24)
        font6.setBold(True)
        font6.setWeight(75)
        self.txt_telacadastro.setFont(font6)
        self.txt_telacadastro.setTextFormat(Qt.PlainText)
        self.txt_telacadastro.setAlignment(Qt.AlignCenter)
        self.txt_telacadastro.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.txt_telacadastro)

        self.txt_caduser = QLabel(self.tela_cadastro)
        self.txt_caduser.setObjectName(u"txt_caduser")
        self.txt_caduser.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setPointSize(19)
        font7.setBold(True)
        font7.setWeight(75)
        self.txt_caduser.setFont(font7)
        self.txt_caduser.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.txt_caduser)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_nome = QLabel(self.tela_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy1.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy1)
        self.txt_nome.setMinimumSize(QSize(135, 48))
        self.txt_nome.setMaximumSize(QSize(135, 48))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.txt_nome.setFont(font8)

        self.horizontalLayout_4.addWidget(self.txt_nome)

        self.entry_nome = QLineEdit(self.tela_cadastro)
        self.entry_nome.setObjectName(u"entry_nome")
        sizePolicy1.setHeightForWidth(self.entry_nome.sizePolicy().hasHeightForWidth())
        self.entry_nome.setSizePolicy(sizePolicy1)
        self.entry_nome.setMinimumSize(QSize(500, 25))
        self.entry_nome.setMaximumSize(QSize(500, 25))
        font9 = QFont()
        font9.setPointSize(9)
        self.entry_nome.setFont(font9)

        self.horizontalLayout_4.addWidget(self.entry_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_user = QLabel(self.tela_cadastro)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy1.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy1)
        self.txt_user.setMinimumSize(QSize(135, 48))
        self.txt_user.setMaximumSize(QSize(135, 48))
        self.txt_user.setFont(font8)

        self.horizontalLayout_5.addWidget(self.txt_user)

        self.entry_user = QLineEdit(self.tela_cadastro)
        self.entry_user.setObjectName(u"entry_user")
        sizePolicy1.setHeightForWidth(self.entry_user.sizePolicy().hasHeightForWidth())
        self.entry_user.setSizePolicy(sizePolicy1)
        self.entry_user.setMinimumSize(QSize(500, 25))
        self.entry_user.setMaximumSize(QSize(500, 25))

        self.horizontalLayout_5.addWidget(self.entry_user)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txt_senha = QLabel(self.tela_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy1.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy1)
        self.txt_senha.setMinimumSize(QSize(135, 48))
        self.txt_senha.setMaximumSize(QSize(135, 48))
        self.txt_senha.setFont(font8)

        self.horizontalLayout_6.addWidget(self.txt_senha)

        self.entry_senha = QLineEdit(self.tela_cadastro)
        self.entry_senha.setObjectName(u"entry_senha")
        self.entry_senha.setMinimumSize(QSize(500, 25))
        self.entry_senha.setMaximumSize(QSize(500, 25))

        self.horizontalLayout_6.addWidget(self.entry_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_csenha = QLabel(self.tela_cadastro)
        self.txt_csenha.setObjectName(u"txt_csenha")
        sizePolicy1.setHeightForWidth(self.txt_csenha.sizePolicy().hasHeightForWidth())
        self.txt_csenha.setSizePolicy(sizePolicy1)
        self.txt_csenha.setMinimumSize(QSize(135, 48))
        self.txt_csenha.setMaximumSize(QSize(135, 48))
        self.txt_csenha.setFont(font8)

        self.horizontalLayout_7.addWidget(self.txt_csenha)

        self.entry_csenha = QLineEdit(self.tela_cadastro)
        self.entry_csenha.setObjectName(u"entry_csenha")
        self.entry_csenha.setMinimumSize(QSize(500, 25))
        self.entry_csenha.setMaximumSize(QSize(500, 25))

        self.horizontalLayout_7.addWidget(self.entry_csenha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txt_perfil = QLabel(self.tela_cadastro)
        self.txt_perfil.setObjectName(u"txt_perfil")
        sizePolicy1.setHeightForWidth(self.txt_perfil.sizePolicy().hasHeightForWidth())
        self.txt_perfil.setSizePolicy(sizePolicy1)
        self.txt_perfil.setMinimumSize(QSize(135, 48))
        self.txt_perfil.setMaximumSize(QSize(135, 48))
        self.txt_perfil.setFont(font8)

        self.horizontalLayout_8.addWidget(self.txt_perfil)

        self.perfil_box = QComboBox(self.tela_cadastro)
        self.perfil_box.addItem("")
        self.perfil_box.addItem("")
        self.perfil_box.setObjectName(u"perfil_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.perfil_box.sizePolicy().hasHeightForWidth())
        self.perfil_box.setSizePolicy(sizePolicy2)
        self.perfil_box.setMinimumSize(QSize(500, 25))
        self.perfil_box.setMaximumSize(QSize(500, 25))

        self.horizontalLayout_8.addWidget(self.perfil_box)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_20 = QLabel(self.tela_cadastro)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_9.addWidget(self.label_20)

        self.btn_cadastrar = QPushButton(self.tela_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(100, 30))
        self.btn_cadastrar.setMaximumSize(QSize(100, 23))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.btn_cadastrar.setFont(font10)

        self.horizontalLayout_9.addWidget(self.btn_cadastrar)

        self.label_21 = QLabel(self.tela_cadastro)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_9.addWidget(self.label_21)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.label_23 = QLabel(self.tela_cadastro)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_10.addWidget(self.label_23)

        self.Pages.addWidget(self.tela_cadastro)

        self.verticalLayout.addWidget(self.Pages)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.Paginas)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_cadastrar_user = QPushButton(self.Paginas)
        self.btn_cadastrar_user.setObjectName(u"btn_cadastrar_user")
        sizePolicy1.setHeightForWidth(self.btn_cadastrar_user.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_user.setSizePolicy(sizePolicy1)
        self.btn_cadastrar_user.setMinimumSize(QSize(200, 45))
        self.btn_cadastrar_user.setMaximumSize(QSize(200, 45))
        self.btn_cadastrar_user.setFont(font10)

        self.horizontalLayout_2.addWidget(self.btn_cadastrar_user)

        self.label_2 = QLabel(self.Paginas)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.Paginas)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        MainWindow.setCentralWidget(self.Paginas)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_cvendas.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR VENDAS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700;\">DIGITALIZADOR P.I</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">v1.0</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">PROJETO INTEGRADOR I</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">UNIVESP</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_25.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DA VENDA", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Numero COO", None))
        self.entry_numerocoo.setPlaceholderText("")
        self.label_5.setText("")
        self.label_18.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Data da Venda", None))
        self.entry_datavenda.setPlaceholderText("")
        self.label_6.setText("")
        self.label_19.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.entry_cpf.setPlaceholderText("")
        self.label_7.setText("")
        self.label_24.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Auto_Ms", None))
        self.entry_automs.setPlaceholderText("")
        self.label_8.setText("")
        self.label_11.setText("")
        self.btn_consultas.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.label_27.setText("")
        self.btn_enviarcad.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_9.setText("")
        self.btn_EscanearDoc.setText(QCoreApplication.translate("MainWindow", u"Escanear Documentos", None))
        self.label_10.setText("")
        self.label_scan1.setText("")
        self.btn_ocrTab1.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar1.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab1.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Cupom/Recibo", None))
        self.label_scan2.setText("")
        self.btn_ocrTab2.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar2.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab2.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Frente Receita", None))
        self.label_scan3.setText("")
        self.btn_ocrTab3.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar3.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab3.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Verso Receita", None))
        self.label_scan4.setText("")
        self.btn_ocrTab4.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar4.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab4.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"Documento", None))
        self.label_scan5.setText("")
        self.btn_ocrTab5.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar5.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab5.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Frente Procura\u00e7\u00e3o", None))
        self.label_scan6.setText("")
        self.btn_ocrTab6.setText(QCoreApplication.translate("MainWindow", u"Converter para Texto", None))
        self.btn_salvar6.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_digitalizarTab6.setText(QCoreApplication.translate("MainWindow", u"Digitalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab6), QCoreApplication.translate("MainWindow", u"Verso Procura\u00e7\u00e3o", None))
        self.label_22.setText("")
        self.txt_telacadastro.setText(QCoreApplication.translate("MainWindow", u"TELA DE CADASTRO", None))
        self.txt_caduser.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_user.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_csenha.setText(QCoreApplication.translate("MainWindow", u"Confirmar senha", None))
        self.txt_perfil.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.perfil_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.perfil_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_20.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_21.setText("")
        self.label_23.setText("")
        self.label.setText("")
        self.btn_cadastrar_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

