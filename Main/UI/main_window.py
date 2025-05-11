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
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_mw_MainWindow(object):
    def setupUi(self, mw_MainWindow):
        if not mw_MainWindow.objectName():
            mw_MainWindow.setObjectName(u"mw_MainWindow")
        mw_MainWindow.resize(1000, 800)
        mw_MainWindow.setMinimumSize(QSize(1000, 800))
        mw_MainWindow.setMaximumSize(QSize(99999, 99999))
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_15)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_17)

        self.line_3 = QFrame(self.groupBox_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.line_3)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_19)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_21)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_23)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_24)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_25)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_26)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_27)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(9, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.gv_main_canvas = QGraphicsView(self.centralwidget)
        self.gv_main_canvas.setObjectName(u"gv_main_canvas")
        brush = QBrush(QColor(199, 199, 199, 255))
        brush.setStyle(Qt.CrossPattern)
        self.gv_main_canvas.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.CrossPattern)
        self.gv_main_canvas.setForegroundBrush(brush1)

        self.gridLayout_2.addWidget(self.gv_main_canvas, 0, 2, 3, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(300, 0))
        self.groupBox_2.setMaximumSize(QSize(300, 9868686))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 2, 1, 1)

        self.le_footing_width = QLineEdit(self.groupBox_2)
        self.le_footing_width.setObjectName(u"le_footing_width")

        self.gridLayout_3.addWidget(self.le_footing_width, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.tl_heel_length = QLabel(self.groupBox_2)
        self.tl_heel_length.setObjectName(u"tl_heel_length")

        self.gridLayout_3.addWidget(self.tl_heel_length, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.le_footing_thickness = QLineEdit(self.groupBox_2)
        self.le_footing_thickness.setObjectName(u"le_footing_thickness")

        self.gridLayout_3.addWidget(self.le_footing_thickness, 1, 1, 1, 1)

        self.tl_footing_thickness = QLabel(self.groupBox_2)
        self.tl_footing_thickness.setObjectName(u"tl_footing_thickness")

        self.gridLayout_3.addWidget(self.tl_footing_thickness, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 3, 2, 1, 1)

        self.le_toe_length = QLineEdit(self.groupBox_2)
        self.le_toe_length.setObjectName(u"le_toe_length")

        self.gridLayout_3.addWidget(self.le_toe_length, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.tl_footing_width = QLabel(self.groupBox_2)
        self.tl_footing_width.setObjectName(u"tl_footing_width")

        self.gridLayout_3.addWidget(self.tl_footing_width, 0, 2, 1, 1)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_grade_difference = QLineEdit(self.groupBox)
        self.le_grade_difference.setObjectName(u"le_grade_difference")

        self.gridLayout.addWidget(self.le_grade_difference, 0, 1, 1, 1)

        self.le_toe_cover = QLineEdit(self.groupBox)
        self.le_toe_cover.setObjectName(u"le_toe_cover")

        self.gridLayout.addWidget(self.le_toe_cover, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tl_toe_cover = QLabel(self.groupBox)
        self.tl_toe_cover.setObjectName(u"tl_toe_cover")

        self.gridLayout.addWidget(self.tl_toe_cover, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.tl_wall_thickness = QLabel(self.groupBox)
        self.tl_wall_thickness.setObjectName(u"tl_wall_thickness")

        self.gridLayout.addWidget(self.tl_wall_thickness, 4, 2, 1, 1)

        self.le_wall_thickness = QLineEdit(self.groupBox)
        self.le_wall_thickness.setObjectName(u"le_wall_thickness")

        self.gridLayout.addWidget(self.le_wall_thickness, 4, 1, 1, 1)

        self.tl_grade_difference = QLabel(self.groupBox)
        self.tl_grade_difference.setObjectName(u"tl_grade_difference")

        self.gridLayout.addWidget(self.tl_grade_difference, 0, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.tl_wall_height = QLabel(self.groupBox)
        self.tl_wall_height.setObjectName(u"tl_wall_height")

        self.gridLayout.addWidget(self.tl_wall_height, 3, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        mw_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 23))
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
        QWidget.setTabOrder(self.le_grade_difference, self.le_toe_cover)
        QWidget.setTabOrder(self.le_toe_cover, self.le_wall_thickness)
        QWidget.setTabOrder(self.le_wall_thickness, self.le_footing_width)
        QWidget.setTabOrder(self.le_footing_width, self.le_footing_thickness)
        QWidget.setTabOrder(self.le_footing_thickness, self.le_toe_length)
        QWidget.setTabOrder(self.le_toe_length, self.gv_main_canvas)

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
        self.groupBox_3.setTitle(QCoreApplication.translate("mw_MainWindow", u"Result Summary", None))
        self.label_6.setText(QCoreApplication.translate("mw_MainWindow", u"Overturning:", None))
        self.label_7.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("mw_MainWindow", u"Sliding:", None))
        self.label_15.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("mw_MainWindow", u"Bearing (US):", None))
        self.label_17.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Shear:", None))
        self.label_19.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Bending:", None))
        self.label_21.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("mw_MainWindow", u"Bearing (SLS):", None))
        self.label_23.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("mw_MainWindow", u"Footing Shear:", None))
        self.label_25.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("mw_MainWindow", u"Foting Bending:", None))
        self.label_27.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mw_MainWindow", u"Footing Dimensions:", None))
        self.label_9.setText(QCoreApplication.translate("mw_MainWindow", u"Heel Length (heel):", None))
        self.label_11.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.label_5.setText(QCoreApplication.translate("mw_MainWindow", u"Toe Length (toe):", None))
        self.tl_heel_length.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("mw_MainWindow", u"Foting Thickness (D):", None))
        self.tl_footing_thickness.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.label_13.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.le_toe_length.setText("")
        self.le_toe_length.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("mw_MainWindow", u"Footing Width (b)", None))
        self.tl_footing_width.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.groupBox.setTitle(QCoreApplication.translate("mw_MainWindow", u"Wall Dimensions:", None))
        self.label_10.setText(QCoreApplication.translate("mw_MainWindow", u"Tow Cover (tc):", None))
        self.label.setText(QCoreApplication.translate("mw_MainWindow", u"Grade Difference (H):", None))
        self.tl_toe_cover.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.label_2.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Thickness (tw):", None))
        self.tl_wall_thickness.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.tl_grade_difference.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.label_12.setText(QCoreApplication.translate("mw_MainWindow", u"mm", None))
        self.label_8.setText(QCoreApplication.translate("mw_MainWindow", u"Wall Height (hwall):", None))
        self.tl_wall_height.setText(QCoreApplication.translate("mw_MainWindow", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("mw_MainWindow", u"Edit", None))
        self.menuDefine.setTitle(QCoreApplication.translate("mw_MainWindow", u"Define", None))
        self.menuRun.setTitle(QCoreApplication.translate("mw_MainWindow", u"Run", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mw_MainWindow", u"Help", None))
    # retranslateUi

