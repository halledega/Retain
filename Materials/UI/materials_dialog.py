# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materials_dialog.ui'
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
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)

class Ui_dl_materials(object):
    def setupUi(self, dl_materials):
        if not dl_materials.objectName():
            dl_materials.setObjectName(u"dl_materials")
        dl_materials.resize(350, 500)
        dl_materials.setMinimumSize(QSize(350, 500))
        dl_materials.setMaximumSize(QSize(350, 500))
        dl_materials.setModal(False)
        self.gridLayout = QGridLayout(dl_materials)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Cancel = QPushButton(dl_materials)
        self.pb_Cancel.setObjectName(u"pb_Cancel")

        self.gridLayout.addWidget(self.pb_Cancel, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gb_concrete = QGroupBox(dl_materials)
        self.gb_concrete.setObjectName(u"gb_concrete")
        self.gb_concrete.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout = QFormLayout(self.gb_concrete)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_concrete)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_name = QLineEdit(self.gb_concrete)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.label_2 = QLabel(self.gb_concrete)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_fc = QLineEdit(self.gb_concrete)
        self.le_fc.setObjectName(u"le_fc")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_fc)

        self.label_3 = QLabel(self.gb_concrete)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.le_unit_weight = QLineEdit(self.gb_concrete)
        self.le_unit_weight.setObjectName(u"le_unit_weight")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_unit_weight)

        self.label_4 = QLabel(self.gb_concrete)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.le_desnity = QLineEdit(self.gb_concrete)
        self.le_desnity.setObjectName(u"le_desnity")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_desnity)

        self.label_5 = QLabel(self.gb_concrete)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.le_alpha1 = QLineEdit(self.gb_concrete)
        self.le_alpha1.setObjectName(u"le_alpha1")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_alpha1)

        self.label_6 = QLabel(self.gb_concrete)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.le_beta1 = QLineEdit(self.gb_concrete)
        self.le_beta1.setObjectName(u"le_beta1")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_beta1)

        self.label_7 = QLabel(self.gb_concrete)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.le_ec = QLineEdit(self.gb_concrete)
        self.le_ec.setObjectName(u"le_ec")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_ec)

        self.label_11 = QLabel(self.gb_concrete)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.le_lambda = QLineEdit(self.gb_concrete)
        self.le_lambda.setObjectName(u"le_lambda")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_lambda)


        self.gridLayout.addWidget(self.gb_concrete, 0, 0, 1, 3)

        self.pb_OK = QPushButton(dl_materials)
        self.pb_OK.setObjectName(u"pb_OK")

        self.gridLayout.addWidget(self.pb_OK, 2, 1, 1, 1)

        self.gb_rebar = QGroupBox(dl_materials)
        self.gb_rebar.setObjectName(u"gb_rebar")
        self.formLayout_2 = QFormLayout(self.gb_rebar)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.gb_rebar)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.lineEdit = QLineEdit(self.gb_rebar)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_9 = QLabel(self.gb_rebar)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_2 = QLineEdit(self.gb_rebar)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.tv_rebarSizes = QTableView(self.gb_rebar)
        self.tv_rebarSizes.setObjectName(u"tv_rebarSizes")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.tv_rebarSizes)

        self.label_10 = QLabel(self.gb_rebar)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)


        self.gridLayout.addWidget(self.gb_rebar, 1, 0, 1, 3)

        QWidget.setTabOrder(self.le_name, self.le_fc)
        QWidget.setTabOrder(self.le_fc, self.le_unit_weight)
        QWidget.setTabOrder(self.le_unit_weight, self.le_desnity)
        QWidget.setTabOrder(self.le_desnity, self.le_alpha1)
        QWidget.setTabOrder(self.le_alpha1, self.le_beta1)
        QWidget.setTabOrder(self.le_beta1, self.le_ec)
        QWidget.setTabOrder(self.le_ec, self.pb_OK)
        QWidget.setTabOrder(self.pb_OK, self.pb_Cancel)

        self.retranslateUi(dl_materials)

        QMetaObject.connectSlotsByName(dl_materials)
    # setupUi

    def retranslateUi(self, dl_materials):
        dl_materials.setWindowTitle(QCoreApplication.translate("dl_materials", u"Materials Definitions", None))
        self.pb_Cancel.setText(QCoreApplication.translate("dl_materials", u"Cancel", None))
        self.gb_concrete.setTitle(QCoreApplication.translate("dl_materials", u"Concrete Properties", None))
        self.label.setText(QCoreApplication.translate("dl_materials", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("dl_materials", u"Compressive Strength (f'c):", None))
        self.label_3.setText(QCoreApplication.translate("dl_materials", u"Unit Weight:", None))
        self.label_4.setText(QCoreApplication.translate("dl_materials", u"Concrete Type:", None))
        self.label_5.setText(QCoreApplication.translate("dl_materials", u"Alpha1:", None))
        self.label_6.setText(QCoreApplication.translate("dl_materials", u"Beta1:", None))
        self.label_7.setText(QCoreApplication.translate("dl_materials", u"Elastic Modulous (Ec):", None))
        self.label_11.setText(QCoreApplication.translate("dl_materials", u"Lambda:", None))
        self.pb_OK.setText(QCoreApplication.translate("dl_materials", u"OK", None))
        self.gb_rebar.setTitle(QCoreApplication.translate("dl_materials", u"Rebar Properties", None))
        self.label_8.setText(QCoreApplication.translate("dl_materials", u"Yield Strength (Fy):", None))
        self.label_9.setText(QCoreApplication.translate("dl_materials", u"Elastic Modulus (E):", None))
        self.label_10.setText(QCoreApplication.translate("dl_materials", u"Bar Sizes:", None))
    # retranslateUi

