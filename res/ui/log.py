# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, PlainTextEdit, PrimaryPushButton, PushButton,
    SimpleCardWidget, SubtitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(934, 810)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(Frame)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.verticalLayout = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.logSubtitleLabel = SubtitleLabel(self.SimpleCardWidget)
        self.logSubtitleLabel.setObjectName(u"logSubtitleLabel")

        self.horizontalLayout_3.addWidget(self.logSubtitleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.logPrimaryPushButton = PrimaryPushButton(self.SimpleCardWidget)
        self.logPrimaryPushButton.setObjectName(u"logPrimaryPushButton")

        self.horizontalLayout_3.addWidget(self.logPrimaryPushButton)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.logPlainTextEdit = PlainTextEdit(self.SimpleCardWidget)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")

        self.verticalLayout.addWidget(self.logPlainTextEdit)


        self.horizontalLayout_2.addWidget(self.SimpleCardWidget)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.logSubtitleLabel.setText(QCoreApplication.translate("Frame", u"\u65e5\u5fd7", None))
        self.logPrimaryPushButton.setText(QCoreApplication.translate("Frame", u"\u6e05\u7a7a\u65e5\u5fd7", None))
    # retranslateUi

