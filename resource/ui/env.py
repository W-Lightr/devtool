# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env.ui'
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

from qfluentwidgets import (BodyLabel, CardWidget, EditableComboBox, LineEdit,
                            PrimaryPushButton, PrimaryPushSettingCard, PushButton, StrongBodyLabel,
                            SubtitleLabel, FluentIcon, PushSettingCard, ConfigItem, FolderValidator)

from config.Config import Config


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(668, 536)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel = SubtitleLabel(Frame)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(Frame)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout_2.addWidget(self.StrongBodyLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rpc_title = BodyLabel(self.CardWidget)
        self.rpc_title.setObjectName(u"rpc_title")

        self.horizontalLayout.addWidget(self.rpc_title)

        self.RpcComboBox = EditableComboBox(self.CardWidget)
        self.RpcComboBox.setObjectName(u"RpcComboBox")

        self.horizontalLayout.addWidget(self.RpcComboBox)

        self.hj_title = BodyLabel(self.CardWidget)
        self.hj_title.setObjectName(u"hj_title")

        self.horizontalLayout.addWidget(self.hj_title)

        self.HjComboBox = EditableComboBox(self.CardWidget)
        self.HjComboBox.setObjectName(u"HjComboBox")

        self.horizontalLayout.addWidget(self.HjComboBox)

        self.mk_title = BodyLabel(self.CardWidget)
        self.mk_title.setObjectName(u"mk_title")

        self.horizontalLayout.addWidget(self.mk_title)

        self.MkComboBox = EditableComboBox(self.CardWidget)
        self.MkComboBox.setObjectName(u"MkComboBox")

        self.horizontalLayout.addWidget(self.MkComboBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.nginxSelect = PushSettingCard('选择',
                                           FluentIcon.DOWNLOAD,
                                           "Nginx目录",
                                           Config().fconfig.get(Config().fconfig.NginxPathFolder),
                                           self.CardWidget)
        self.nginxSelect.setObjectName(u"nginxCard")
        self.nginxSelect.setGeometry(QRect(20, 100, 621, 61))

        self.verticalLayout_2.addWidget(self.nginxSelect)

        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Frame)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.verticalLayout_3.addWidget(self.StrongBodyLabel_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.jiazaiConfigBtn = PrimaryPushButton(self.CardWidget_2)
        self.jiazaiConfigBtn.setObjectName(u"jiazaiConfigBtn")

        self.horizontalLayout_2.addWidget(self.jiazaiConfigBtn)

        self.huanyuanConfigBtn = PrimaryPushButton(self.CardWidget_2)
        self.huanyuanConfigBtn.setObjectName(u"huanyuanConfigBtn")

        self.horizontalLayout_2.addWidget(self.huanyuanConfigBtn)

        self.startNginxBtn = PrimaryPushButton(self.CardWidget_2)
        self.startNginxBtn.setObjectName(u"startNginxBtn")

        self.horizontalLayout_2.addWidget(self.startNginxBtn)

        self.stopNginxBtn = PrimaryPushButton(self.CardWidget_2)
        self.stopNginxBtn.setObjectName(u"stopNginxBtn")

        self.horizontalLayout_2.addWidget(self.stopNginxBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout.addWidget(self.CardWidget_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", u"\u73af\u5883\u5207\u6362", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"\u914d\u7f6e", None))
        self.rpc_title.setText(QCoreApplication.translate("Frame", u"RPC\u914d\u7f6e", None))
        self.hj_title.setText(QCoreApplication.translate("Frame", u"\u73af\u5883", None))
        self.mk_title.setText(QCoreApplication.translate("Frame", u"\u6a21\u5757", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Frame", u"\u64cd\u4f5c", None))
        self.jiazaiConfigBtn.setText(QCoreApplication.translate("Frame", u"\u52a0\u8f7d\u914d\u7f6e", None))
        self.huanyuanConfigBtn.setText(QCoreApplication.translate("Frame", u"\u8fd8\u539f\u914d\u7f6e", None))
        self.startNginxBtn.setText(QCoreApplication.translate("Frame", u"\u542f\u52a8Nginx", None))
        self.stopNginxBtn.setText(QCoreApplication.translate("Frame", u"\u5173\u95edNgin", None))
    # retranslateUi
