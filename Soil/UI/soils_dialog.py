# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'soils_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_dl_soils(object):
    def setupUi(self, dl_soils):
        if not dl_soils.objectName():
            dl_soils.setObjectName(u"dl_soils")
        dl_soils.resize(350, 500)
        dl_soils.setMinimumSize(QSize(350, 500))
        dl_soils.setMaximumSize(QSize(350, 500))
        dl_soils.setModal(False)
        self.gridLayout = QGridLayout(dl_soils)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Cancel = QPushButton(dl_soils)
        self.pb_Cancel.setObjectName(u"pb_Cancel")

        self.gridLayout.addWidget(self.pb_Cancel, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.groupBox = QGroupBox(dl_soils)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_name = QLineEdit(self.groupBox)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_unitWeight = QLineEdit(self.groupBox)
        self.le_unitWeight.setObjectName(u"le_unitWeight")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_unitWeight)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.le_ulsBearing = QLineEdit(self.groupBox)
        self.le_ulsBearing.setObjectName(u"le_ulsBearing")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_ulsBearing)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.le_slsBearing = QLineEdit(self.groupBox)
        self.le_slsBearing.setObjectName(u"le_slsBearing")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_slsBearing)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.le_frictionCoeff = QLineEdit(self.groupBox)
        self.le_frictionCoeff.setObjectName(u"le_frictionCoeff")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_frictionCoeff)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.le_activeCoeff = QLineEdit(self.groupBox)
        self.le_activeCoeff.setObjectName(u"le_activeCoeff")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_activeCoeff)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.le_passiveCoeff = QLineEdit(self.groupBox)
        self.le_passiveCoeff.setObjectName(u"le_passiveCoeff")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_passiveCoeff)

        self.te_messages = QTextEdit(self.groupBox)
        self.te_messages.setObjectName(u"te_messages")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.te_messages)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.pb_OK = QPushButton(dl_soils)
        self.pb_OK.setObjectName(u"pb_OK")

        self.gridLayout.addWidget(self.pb_OK, 1, 1, 1, 1)

        QWidget.setTabOrder(self.le_name, self.le_unitWeight)
        QWidget.setTabOrder(self.le_unitWeight, self.le_ulsBearing)
        QWidget.setTabOrder(self.le_ulsBearing, self.le_slsBearing)
        QWidget.setTabOrder(self.le_slsBearing, self.le_frictionCoeff)
        QWidget.setTabOrder(self.le_frictionCoeff, self.le_activeCoeff)
        QWidget.setTabOrder(self.le_activeCoeff, self.le_passiveCoeff)
        QWidget.setTabOrder(self.le_passiveCoeff, self.pb_OK)
        QWidget.setTabOrder(self.pb_OK, self.pb_Cancel)

        self.retranslateUi(dl_soils)

        QMetaObject.connectSlotsByName(dl_soils)
    # setupUi

    def retranslateUi(self, dl_soils):
        dl_soils.setWindowTitle(QCoreApplication.translate("dl_soils", u"Soil Definitions", None))
        self.pb_Cancel.setText(QCoreApplication.translate("dl_soils", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("dl_soils", u"Soil Properties", None))
        self.label.setText(QCoreApplication.translate("dl_soils", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("dl_soils", u"Unit Weight: (kN/m3)", None))
        self.label_3.setText(QCoreApplication.translate("dl_soils", u"ULS Bearing: (kPa)", None))
        self.label_4.setText(QCoreApplication.translate("dl_soils", u"SLS Bearing: (kPa)", None))
        self.label_5.setText(QCoreApplication.translate("dl_soils", u"Friction Coefficient:", None))
        self.label_6.setText(QCoreApplication.translate("dl_soils", u"Active Pressuure Coefficient:", None))
        self.label_7.setText(QCoreApplication.translate("dl_soils", u"Passive Pressure Coefficient:", None))
        self.pb_OK.setText(QCoreApplication.translate("dl_soils", u"OK", None))
    # retranslateUi

