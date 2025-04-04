# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_mw_MainWindow(object):
    def setupUi(self, mw_MainWindow):
        if not mw_MainWindow.objectName():
            mw_MainWindow.setObjectName(u"mw_MainWindow")
        mw_MainWindow.resize(835, 591)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        mw_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 33))
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
        self.menuFile.setTitle(QCoreApplication.translate("mw_MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("mw_MainWindow", u"Edit", None))
        self.menuDefine.setTitle(QCoreApplication.translate("mw_MainWindow", u"Define", None))
        self.menuRun.setTitle(QCoreApplication.translate("mw_MainWindow", u"Run", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mw_MainWindow", u"Help", None))
    # retranslateUi

