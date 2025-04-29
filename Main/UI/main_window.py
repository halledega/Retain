# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGraphicsView,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_mw_MainWindow(object):
    def setupUi(self, mw_MainWindow):
        if not mw_MainWindow.objectName():
            mw_MainWindow.setObjectName(u"mw_MainWindow")
        mw_MainWindow.resize(1000, 800)
        mw_MainWindow.setMinimumSize(QSize(1000, 800))
        mw_MainWindow.setMaximumSize(QSize(1000, 800))
        self.a_about = QAction(mw_MainWindow)
        self.a_about.setObjectName(u"a_about")
        self.a_new = QAction(mw_MainWindow)
        self.a_new.setObjectName(u"a_new")
        self.a_open = QAction(mw_MainWindow)
        self.a_open.setObjectName(u"a_open")
        self.a_save = QAction(mw_MainWindow)
        self.a_save.setObjectName(u"a_save")
        self.a_saveas = QAction(mw_MainWindow)
        self.a_saveas.setObjectName(u"a_saveas")
        self.a_exit = QAction(mw_MainWindow)
        self.a_exit.setObjectName(u"a_exit")
        self.a_preferences = QAction(mw_MainWindow)
        self.a_preferences.setObjectName(u"a_preferences")
        self.a_defineSoil = QAction(mw_MainWindow)
        self.a_defineSoil.setObjectName(u"a_defineSoil")
        self.a_defineMaterials = QAction(mw_MainWindow)
        self.a_defineMaterials.setObjectName(u"a_defineMaterials")
        self.a_defineSurchargeLoads = QAction(mw_MainWindow)
        self.a_defineSurchargeLoads.setObjectName(u"a_defineSurchargeLoads")
        self.a_defineWallLoads = QAction(mw_MainWindow)
        self.a_defineWallLoads.setObjectName(u"a_defineWallLoads")
        self.a_defineSeismicLoads = QAction(mw_MainWindow)
        self.a_defineSeismicLoads.setObjectName(u"a_defineSeismicLoads")
        self.centralwidget = QWidget(mw_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.hs_wall_height = QSlider(self.groupBox)
        self.hs_wall_height.setObjectName(u"hs_wall_height")
        self.hs_wall_height.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.hs_wall_height)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.hs_wall_thickness = QSlider(self.groupBox)
        self.hs_wall_thickness.setObjectName(u"hs_wall_thickness")
        self.hs_wall_thickness.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.hs_wall_thickness)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.hs_footing_width = QSlider(self.groupBox)
        self.hs_footing_width.setObjectName(u"hs_footing_width")
        self.hs_footing_width.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.hs_footing_width)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.hs_footing_thickness = QSlider(self.groupBox)
        self.hs_footing_thickness.setObjectName(u"hs_footing_thickness")
        self.hs_footing_thickness.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.hs_footing_thickness)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.hs_toe_length = QSlider(self.groupBox)
        self.hs_toe_length.setObjectName(u"hs_toe_length")
        self.hs_toe_length.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.hs_toe_length)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.line)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_7)


        self.horizontalLayout.addWidget(self.groupBox)

        self.gv_main_canvas = QGraphicsView(self.centralwidget)
        self.gv_main_canvas.setObjectName(u"gv_main_canvas")
        brush = QBrush(QColor(199, 199, 199, 255))
        brush.setStyle(Qt.CrossPattern)
        self.gv_main_canvas.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.CrossPattern)
        self.gv_main_canvas.setForegroundBrush(brush1)

        self.horizontalLayout.addWidget(self.gv_main_canvas)

        mw_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuDefine = QMenu(self.menubar)
        self.menuDefine.setObjectName(u"menuDefine")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mw_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mw_MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDefine.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.a_new)
        self.menuFile.addAction(self.a_open)
        self.menuFile.addAction(self.a_save)
        self.menuFile.addAction(self.a_saveas)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.a_preferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.a_exit)
        self.menuDefine.addAction(self.a_defineSoil)
        self.menuDefine.addAction(self.a_defineMaterials)
        self.menuDefine.addAction(self.a_defineSurchargeLoads)
        self.menuDefine.addAction(self.a_defineWallLoads)
        self.menuDefine.addAction(self.a_defineSeismicLoads)
        self.menuHelp.addAction(self.a_about)

        self.retranslateUi(mw_MainWindow)

        QMetaObject.connectSlotsByName(mw_MainWindow)
    # setupUi

    def retranslateUi(self, mw_MainWindow):
        mw_MainWindow.setWindowTitle(QCoreApplication.translate("mw_MainWindow", u"MainWindow", None))
        self.a_about.setText(QCoreApplication.translate("mw_MainWindow", u"About", None))
        self.a_new.setText(QCoreApplication.translate("mw_MainWindow", u"New", None))
        self.a_open.setText(QCoreApplication.translate("mw_MainWindow", u"Open", None))
        self.a_save.setText(QCoreApplication.translate("mw_MainWindow", u"Save", None))
        self.a_saveas.setText(QCoreApplication.translate("mw_MainWindow", u"Save As", None))
        self.a_exit.setText(QCoreApplication.translate("mw_MainWindow", u"Exit", None))
        self.a_preferences.setText(QCoreApplication.translate("mw_MainWindow", u"Preferences", None))
        self.a_defineSoil.setText(QCoreApplication.translate("mw_MainWindow", u"Soil", None))
        self.a_defineMaterials.setText(QCoreApplication.translate("mw_MainWindow", u"Materials", None))
        self.a_defineSurchargeLoads.setText(QCoreApplication.translate("mw_MainWindow", u"Surcharge Loads", None))
        self.a_defineWallLoads.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Loads", None))
        self.a_defineSeismicLoads.setText(QCoreApplication.translate("mw_MainWindow", u"Semsic Loads", None))
        self.groupBox.setTitle(QCoreApplication.translate("mw_MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Height:", None))
        self.label_2.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Thickness:", None))
        self.label_3.setText(QCoreApplication.translate("mw_MainWindow", u"Footing Width:", None))
        self.label_4.setText(QCoreApplication.translate("mw_MainWindow", u"Foting Thickness:", None))
        self.label_5.setText(QCoreApplication.translate("mw_MainWindow", u"Toe Length:", None))
        self.label_6.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Dimensions:", None))
        self.label_7.setText(QCoreApplication.translate("mw_MainWindow", u"Footing Dimensionms:", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("mw_MainWindow", u"Edit", None))
        self.menuDefine.setTitle(QCoreApplication.translate("mw_MainWindow", u"Define", None))
        self.menuRun.setTitle(QCoreApplication.translate("mw_MainWindow", u"Run", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mw_MainWindow", u"Help", None))
    # retranslateUi

