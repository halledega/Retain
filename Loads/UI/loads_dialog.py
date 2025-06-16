# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loads_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_dl_loads(object):
    def setupUi(self, dl_loads):
        if not dl_loads.objectName():
            dl_loads.setObjectName(u"dl_loads")
        dl_loads.resize(524, 300)
        dl_loads.setMinimumSize(QSize(500, 300))
        dl_loads.setMaximumSize(QSize(524, 300))
        self.gridLayout_2 = QGridLayout(dl_loads)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(dl_loads)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(200, 0))
        self.groupBox_2.setMaximumSize(QSize(200, 16777215))
        self.groupBox_2.setMouseTracking(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_new = QPushButton(self.groupBox_2)
        self.pb_new.setObjectName(u"pb_new")

        self.gridLayout_3.addWidget(self.pb_new, 1, 0, 1, 1)

        self.pb_delete = QPushButton(self.groupBox_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.gridLayout_3.addWidget(self.pb_delete, 1, 1, 1, 1)

        self.lb_loads = QListWidget(self.groupBox_2)
        self.lb_loads.setObjectName(u"lb_loads")

        self.gridLayout_3.addWidget(self.lb_loads, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(dl_loads)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.cb_type = QComboBox(self.groupBox)
        self.cb_type.setObjectName(u"cb_type")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_type)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.le_name = QLineEdit(self.groupBox)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_name)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.le_value = QLineEdit(self.groupBox)
        self.le_value.setObjectName(u"le_value")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_value)

        self.tl_units = QLabel(self.groupBox)
        self.tl_units.setObjectName(u"tl_units")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tl_units)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.cb_category = QComboBox(self.groupBox)
        self.cb_category.setObjectName(u"cb_category")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_category)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)

        self.pb_save = QPushButton(self.groupBox)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setMinimumSize(QSize(0, 0))
        self.pb_save.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pb_save)


        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 2)

        self.pb_Cancel = QPushButton(dl_loads)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        self.pb_Cancel.setMinimumSize(QSize(0, 0))
        self.pb_Cancel.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pb_Cancel, 2, 2, 1, 1)

        self.pb_OK = QPushButton(dl_loads)
        self.pb_OK.setObjectName(u"pb_OK")
        self.pb_OK.setMinimumSize(QSize(0, 0))
        self.pb_OK.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pb_OK, 2, 1, 1, 1)


        self.retranslateUi(dl_loads)

        QMetaObject.connectSlotsByName(dl_loads)
    # setupUi

    def retranslateUi(self, dl_loads):
        dl_loads.setWindowTitle(QCoreApplication.translate("dl_loads", u"Edit Load", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dl_loads", u"Load List", None))
        self.pb_new.setText(QCoreApplication.translate("dl_loads", u"New", None))
        self.pb_delete.setText(QCoreApplication.translate("dl_loads", u"Delete", None))
        self.groupBox.setTitle(QCoreApplication.translate("dl_loads", u"Load Properties", None))
        self.label_3.setText(QCoreApplication.translate("dl_loads", u"Type:", None))
        self.label.setText(QCoreApplication.translate("dl_loads", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("dl_loads", u"Value:", None))
        self.tl_units.setText("")
        self.label_4.setText(QCoreApplication.translate("dl_loads", u"Category:", None))
        self.pb_save.setText(QCoreApplication.translate("dl_loads", u"Save", None))
        self.pb_Cancel.setText(QCoreApplication.translate("dl_loads", u"Cancel", None))
        self.pb_OK.setText(QCoreApplication.translate("dl_loads", u"OK", None))
    # retranslateUi

